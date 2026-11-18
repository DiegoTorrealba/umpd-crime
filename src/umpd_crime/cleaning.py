import re
import pandas as pd

def normalize_road(road_str): 
  """GPT-6.1 Sol Medium-assisted function in standardizing road names and and abbreviations in road names."""
  road = " ".join(road_str.casefold().split())
    # casefold makes text lowercase
  
  suffixes = {
    "road": "rd",
    "avenue": "ave",
    "street": "st",
    "drive": "dr",
    "lane": "ln",
    "boulevard" : 'blvd',
    'parkway': 'pkwy',
    'court': 'ct',
    'place': "pl",
    'terrace': 'ter',
    'trail' : 'trl'
  }
  
  words = road.split()
  if words:
    ending = words[-1].rstrip(".") # removes period from street name or abbreviation
    words[-1] = suffixes.get(ending, ending) # swaps out spelled out road part for abbreviation
  
  return " ".join(words).title() # returns lowercase string as title case

def classify_change(original, cleaned):
  """Takes the original and cleaned locations and classifies the changes/differences between the two after my cleaning steps; created with the assistance of GPT-6.1 Sol Medium"""
  if pd.isna(original) and pd.isna(cleaned):
    return 'Unchanged'
  
  if pd.isna(original) or pd.isna(cleaned):
    return "Other change"
  
  if original == cleaned:
    return "Unchanged"
  
  # Matches cleaned coordinate format: "(latitude, longitude)"
  if re.fullmatch(
    r"\([+-]?\d+\.\d+,\s*[+-]?\d+\.\d+\)",
    cleaned
  ):
    return "Coordinates extracted"
  
  # Check that the cleaned value is exactly the final address
  name, sep, address = original.rpartition(" at ")
  if sep and cleaned == address:
    return "Address extracted from a building description"
  
  if "/" in original:
    if "&" in cleaned:
      return "Intersection standardized"
    
    parts = original.split("/")
    if len(parts) == 2:
      road_1, road_2 = [normalize_road(part) for part in parts]
      
      if road_1 == road_2 == normalize_road(cleaned):
        return "Same-road pair reduced to one road"
  
  return "Other change"
    
def is_standard_address(location_str): 
  """GPT-6.1 Sol Medium-assisted created function that helps detect standard address strings, including those with 'block of' """
  address_pattern = re.compile(
    r"""
    \d+[A-Z]?                         # Street number, optionally with a letter
    [ \t]+
    (?:block[ \t]+of[ \t]+)?           # Optional "block of"
    [A-Z0-9][A-Z0-9.'’\-]*             # First word of street name
    (?:[ \t]+[A-Z0-9][A-Z0-9.'’\-]*)*  # Additional street-name words
    [ \t]+
    (?:                               # Recognized street types
        Rd|Road|Ave|Avenue|St|Street|
        Dr|Drive|Ln|Lane|Blvd|Boulevard|
        Ct|Court|Pl|Place|Way|Row|
        Ter|Terrace|Trl|Trail|Cir|Circle|
        Hwy|Highway|Pkwy|Pky|Parkway|
        Aly|Alley|Loop|Glen|Ellipse
    )
    \.?
    (?:[ \t]+(?:N|S|E|W|NE|NW|SE|SW))? # Optional direction after street type
    """,
    flags=re.IGNORECASE | re.VERBOSE
  )
  
  if not isinstance(location_str, str):
    return False
  
  return address_pattern.fullmatch(location_str.strip()) is not None

def clean_location(location_str):
  """GPT-6.1 Sol Medium-assisted created function that helps clean the location columns of the dataframe when nonstandard address"""
  if not isinstance(location_str, str):
    return location_str
  
  # extracting coordinates from coordinate locations 
  coordinate_pattern = re.compile(
    r"(?<![\w.])"
    r"(?P<latitude>[+-]?\d{1,3}\.\d+)"
    r"\s*;\s*"
    r"(?P<longitude>[+-]?\d{1,3}\.\d+)"
    r"(?![\w.])"
  )
  
  coordinate_match = coordinate_pattern.search(location_str)
  if coordinate_match: 
    latitude = float(coordinate_match.group('latitude'))
    longitude = float(coordinate_match.group('longitude'))
    
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
      return f"({latitude}, {longitude})"
    else:
      return location_str
  
  # trying to fix intersections
  if location_str.count('/') == 1:
    parts = [part.strip() for part in location_str.split('/')]
    
    if all(parts):
      road_ending = (
        r"\b(?:Rd|Road|Ave|Avenue|St|Street|Dr|Drive|"
        r"Ln|Lane|Blvd|Boulevard|Pkwy|Parkway|"
        r"Ct|Court|Pl|Place|Way|Ter|Terrace|Trl|Trail|"
        r"Cir|Circle|Row|Pike|Hwy|Highway)\.?$"
      )
      
      both_roads = all(re.search(road_ending, part, flags=re.IGNORECASE) for part in parts)
      has_numbers = any(re.search(r"\d", part) for part in parts)
      
      if both_roads or not has_numbers: 
        place_1, place_2 = sorted(normalize_road(part) for part in parts)
        
        if place_1 == place_2:
          return place_1
        
        return f"{place_1} & {place_2}"
  
  # trying to fit name at address pattern
  # name, separator will be "" if " at " is not present
  name, separator, address = location_str.rpartition(' at ')
  
  if separator and re.match(r"^\d+[A-Za-z]?\s+\S", address):
    return address
  
  return location_str
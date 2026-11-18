import os
import time
import requests
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium as fl

GOOGLE_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

def get_shapely_point(latitude, longitude):
  point = Point(longitude, latitude)
  return point

def create_markers_for_flmap(gdf, flmap, marker_color = "blue"): 
    if not isinstance(gdf, gpd.GeoDataFrame):
        print("gdf must be a Geopandas GeoDataFrame.")
        return

    for row in gdf.itertuples():

        if pd.isna(row[2]) or pd.isna(row[3]):
            continue
        
        fl.Marker(
            location = [row[2], row[3]],
            popup = row[1],
            tooltip = f"Source location: {row[1]}\nLatitude: {row[2]}\nLongitude: {row[3]}",
            icon = fl.Icon(color = marker_color, icon="info-sign")
        ).add_to(flmap)

def google_geocode_addrs(addresses, headers):
  if not addresses:
    print("Pass a valid list of addresses")
    return None
  else:
    google_params = {
    'address': None,
    'bounds': '38.883790,-77.065390|39.081929,-76.810495',
    'key': os.getenv("UMPDCRIMEGOOGLEGEOCODINGAPIKEY")
    }
    results = []
    start_time = time.time()
    num_missed = 0
    
    perc_25 = round(len(addresses) * .25)
    perc_50 = round(len(addresses) * .50)
    perc_75 = round(len(addresses) * .75)
    
    for i, addr in enumerate(addresses):
      
      if i == perc_25:
        print("25% geocoding done")
      elif i == perc_50:
        print("50% goeocoding done")
      elif i == perc_75:
        print('75% geocoding done')
      
      result_dict = {'source_location': addr, 'latitude': None, 'longitude': None}
      google_params['address'] = addr
      
      response = requests.get(GOOGLE_BASE_URL, params=google_params, headers=headers)
      
      if response.status_code != 200:
        print(f"Received {response.status_code} status code for '{addr}': {response.reason}; using None for latitude and longitude")
        results.append(result_dict)
        num_missed += 1
        continue
      
      data = response.json()
      try:
        returned_geometry = data['results'][0]['geometry']['location']
      except (IndexError, KeyError) as e:
        print(f"Data did not return with correct JSON structure for {addr}; setting None for latitude and longitude")
        results.append(result_dict)
        num_missed += 1
        continue
      
      result_dict['latitude'] = returned_geometry['lat']
      result_dict['longitude'] = returned_geometry['lng']
      
      results.append(result_dict)
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print(
          f"Took {total_time:.2f} seconds to Google Geocode {len(addresses)} locations"
          f"\n\tSuccesses: {len(addresses) - num_missed}"
          f"\n\tFailures: {num_missed}"
          )  
    
    df = pd.DataFrame(results)
    df['point'] = df.apply(lambda row: get_shapely_point(row['latitude'], row['longitude']), axis=1)
    gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df['longitude'], df['latitude']), crs="EPSG:4326")
    
    return gdf

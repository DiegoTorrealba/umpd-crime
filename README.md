# UMPD Crime Scraper and Analysis

## Description

This project scrapes [University of Maryland Police Department (College Park)](https://umpd.umd.edu/)'s [Annual Arrest Logs](https://umpd.umd.edu/statistics-reports/arrest-logs) and [Daily Crime and Incident Logs](https://umpd.umd.edu/statistics-reports/daily-crime-and-incident-logs), cleans the scraped logs, uses entity extraction methods to parse the arrest description, and runs NLP/AI analyses on the descriptions to answer the overarching questions of **what does incidents and arrests look like at UMD/College Park, and where are they located?**
## Project outline
- This project uses uv to manage dependencies.
```
umpd-crime/
|- .gitignore
|- .python-version
|- .venv/
|- pyproject.toml
|- uv.lock
|- README.md ( this file <3 )
|- data/
	|- raw/
	└- processed/
|- notebooks/ 
	|-pipeline-notebooks/ # actual notebooks to be ran if needed
	└-testing-notebooks/ # development notebooks
|- outputs/ # visualization outputs
|- scripts/ # Pipeline scripts to be ran via `uv run python scripts/...`
|- src/
	|- umpd_crime/ # Python package points
		└- __init__.py
```
## Proposed methodology
1. Programmatically web scrape logs from UMPD Statistics & Reports using BeautifulSoup. 
2. Combine incident reports and turn incidents and arrests into respective pandas dataframes. 
3. Geocode arrests based on available address and convert dataframe into geopandas geodataframe. 
4. Aggregate geospatial coordinates by neighborhood/area and calculate their respective arrest counts. 
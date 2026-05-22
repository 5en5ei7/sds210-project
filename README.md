---------------------------------------------------------------------------------------------------------

# SDS-210: Near Real-Time Wildfire Population Proximity Assessment for Australia

---------------------------------------------------------------------------------------------------------

## Description
This project assesses wildfire proximity to population in Australia using near-real-time satellite 
fire detection data from NASA FIRMS. Fire detections are spatially filtered to Australia and spatially clustered
into fire events. The Population Proximity is calculated by summing all estimated total number of people 
within a 3 km buffer around each clustered fire event. The fire detections dataset is derived using a one day range
to ensure recent observations.

An interactive map visualizes fire event locations and provides an estimate of potentially affected people nearby. 
Additional fire attributes are available via pop-up and a quantitative analysis summarizes the results of the project.

## Research Question
Which recent fire events in Australia contain the highest estimated population within a 3km radius?

## Project Structure
```
sds210-final-project
|--- data/    # Raw and processed input data for project
      |--- raw/
      |--- processed/
|--- notebooks/   # Jupyter notebook 
|--- outputs/   # Output files from analysis and visualization (e.g. plots, maps, ...)
|--- scr/   # helper functions 
|--- .gitignore   # files that should be ignored when pushed up on github (e.g. raster files)
|--- environment.yml    # lists all installed packages
|--- README.md    # instructions to recreate project; additional informations on project
```

## Setup
1. Clone the repository
2. Download the data files and place them in `data/raw`
  - Spatial Distribution of Population, Australia,2026:
  https://hub.worldpop.org/geodata/summary?id=72432
  Label as "aus_pop_2025_CN_100m_R2025A_v1.tif"
  
  - States and Territories Australia from year 2021: 
  https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files 
  Label as "states_australia_2021.shp"
  
  -Note: The FIRMS-Fire data are accessed through the API in the notebook!
  You might use the API to access data, therefore you need a valid map key.
  Map key can be generated via: https://firms.modaps.eosdis.nasa.gov/api/map_key/
  - For full reproducibility: place 'fire_data_api_request_20260521.csv' in data/processed/
3. Create the environment:
```bash
(base) C:\Users\flo>conda create -n sds-final-project python=3.14.4
```
4. Activate the environment:
```bash
(base) C:\Users\flo>conda activate sds-final-project
```
5. Install packages via .yml file:
```bash
(sds-final-project) C:\Users\flo\Uni\SDS210\sds210-project>conda env update -f environment.yml
```
6. Create Kernel: 
```bash
(sds-final-project) C:\Users\flo\Uni\SDS210\sds210-project>python -m ipykernel install --user --name sds-final-project --display-name "SDS Final Project"
```
7. Run the notebook for example in VisualStudioCode from the project root
8. Deactivate environment
```bash
(sds-final-project) C:\Users\flo\Uni\SDS210\sds210-project>conda deactivate
```

## Data Sources
- FIRMS Fire Data: https://firms.modaps.eosdis.nasa.gov/
- Australia Border Shapefile: https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files 
- Population Count from year 2026: https://hub.worldpop.org/geodata/summary?id=72432

## Author
Florian Dörig, Course SDS-210, University of Zürich, Spring semester 2026



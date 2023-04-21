# SI507_Final_Project

This project generates an interactive map of Michigan trails and campgrounds.
It also provides the ability to filter the map based on a specific county.

## Required Python Packages

- xmltodict
- pandas
- numpy
- folium

## How to run

1. Install the required packages using pip: 
  pip install xmltodict pandas numpy folium

2. Ensure the following XML files are in the same directory as the Python script:

- Campground.XML
- CampingFeaturesOptions.XML
- CampingTrailAssoc.XML
- County.XML
- Features.XML
- Trail.XML
- TrailCounties.XML
- TrailFeaturesOptions.XML
- TrailSurface.XML

3. Open the Jupyter Notebook file (si507_Final_Project.ipynb) using Jupyter Notebook, Jupyter Lab, or VSStudioCode.

4. If you wish to create a map of a certain county other than Washtenaw county (default), please replace 'Washtenaw' with any other Michigan county in 'county_name' in the 'filter_data_by_county' block.

5. Run all cells in the notebook (except for the last cell if you don't want the county map).

6. The notebook will generate and save an interactive map named "michigan_map.html" and a map filtered by county named "{county}_name_map.html", with {county} being whatever county you specify in 'county_name'.

7. Click on the specific map ("michigan_map.html" or "{county}_name_map.html") to view an interactive map of Michigan trails and campgrounds or a specific county's trails and campgrounds.

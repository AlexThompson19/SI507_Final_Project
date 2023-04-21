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

## Data Structure

The data structure used in this project is a tree, which represents the hierarchical organization of Michigan's counties, trails, campgrounds, and features.

### Tree Structure

The tree structure is composed of nodes, where each node has a `data` attribute and a list of `children`. The `data` attribute holds the information for a specific entity, such as a county, trail, campground, or feature. The `children` attribute is a list of child nodes under the current node.

Here's the hierarchy of the tree structure:

1. Michigan (root node)
   - County
     - Trail
       - Campground
         - Feature

The tree is constructed using the `TreeNode` class in the Jupyter Notebook file (si507_Final_Project.ipynb), and it's built using the data from the XML files.

### Saving and Loading Tree Structure

The tree structure is saved as a JSON file named "michigan_tree.json" using the `tree_to_dict` function in the Jupyter Notebook file (si507_Final_Project.ipynb). This function converts the tree structure into a nested dictionary format that can be saved as a JSON file.

To load the JSON file and reconstruct the tree, the `dict_to_tree` function is used. This function reads the JSON file and converts the nested dictionary back into a tree structure using the `TreeNode` class.

### Interacting with the Tree Structure

The tree structure can be traversed and filtered to access specific data or generate maps based on the selected criteria, such as filtering data by county.

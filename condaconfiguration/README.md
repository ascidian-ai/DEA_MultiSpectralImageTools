# SETTING UP A CONDA ENVIRONMENT IN ANACONDA

Last Updated: 10-Apr-2022

### Installing the environment
#### Pre-requisites
- Anaconda installed on Windows Environment
- [Copy this conda environment configuration file](environment.yml) to a local directory

#### Installation steps
To setup a new environment with Conda follow these steps:

1) Launch Anaconda

2) Goto to the "base" environment

3) Launch Command Prompt

4) Run the following commands:

&emsp;&emsp;&gt;cd {directory containing the environment.yml file}

&emsp;&emsp;&gt;conda env create -f environment.yml

5) In Anaconda install JupyterNotebook


### Removing the environment
To remove the environment repeat steps 1 through 3 above then run the following command

&emsp;&emsp;&gt;conda env remove -n DEAGeospatialAnalysis

### Environment Packages
The following packages make up the DEAGeospatialAnalysis environment.<br>

#### CORE
**requests**<br>
A common library for managing HTTP requests.<br>

#### DATA ENGINEERING
**numpy**<br>
Numpy is a library designed for efficient array computation.<br>
**pandas**<br>
Data structures for data analysis, time series, and statistics.<br>

#### DATA SCIENCE/ML
**scikit-learn**<br>
Sci-kit Learn is a popular Machine/Statitical learning package.<br>

#### VISUALISATION AND IMAGE PROCESSING
**matplotlib**<br>
MatplotLib is a plotting Library for static, animated, and interactive visualizations.<br>
**seaborn**<br>
Seaborn extends MatPlotlib with more sophisticated plot types.<br>
**plotly**<br>
Plotly allows the creation of interactive graphs, plots and maps.<br>

#### GEOSPATIAL
**pyproj**<br>
An interface to PROJ (cartographic projections and coordinate transformations library).<br>
**shapely**<br>
Shapely supports manipulation and analysis of geometric objects in the Cartesian plane.<br>
**descartes**<br>
Allows using Shapely or GeoJSON-like geometric objects as matplotlib paths and patches.<br>
Requires: matplotlib, numpy, and optionally Shapely 1.2+.
**geopandas**<br>
Geopandas extends the datatypes used by Pandas to allow spatial operations on geometric types.<br>
Geometric operations are performed by shapely.<br>
Geopandas further depends on fiona for file access and matplotlib for plotting.<br>
**geopy**<br>
A Python client for several popular geocoding web services.<br>
Geopy includes geocoder classes for the OpenStreetMap, Google Geocoding API (V3), and many other geocoding services.
**folium**<br>
Folium makes it easy to visualize data that’s been manipulated in Python on an interactive leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing rich vector/raster/HTML visualizations as markers on the map.<br>
The library has a number of built-in tilesets from OpenStreetMap, Mapbox, and Stamen, and supports custom tilesets with Mapbox or Cloudmade API keys. folium supports both Image, Video, GeoJSON and TopoJSON overlays.<br>
**pystac-client**<br>
The STAC Python Client (pystac_client) is a Python package for working with STAC Catalogs and APIs that conform to the [STAC](https://github.com/radiantearth/stac-spec) and [STAC API](https://github.com/radiantearth/stac-api-spec) specs in a seamless way. PySTAC Client builds upon PySTAC through higher-level functionality and ability to leverage STAC API search endpoints.<br>
**odc-client**<br>
The odc-stac library allows downloads of DEA datasets stored in AWS. When accessing AWS (like outside the DEA sandbox), AWS signed requests must be disabled<br>

#### DIGITAL EARTH AUSTRALIA/AFRICA (DEA) SPECIFIC LIBRARIES
**dea-tools**<br>
Python functions and algorithms developed to assist in analysing Digital Earth Australia (DEA) data (e.g. loading data, plotting, spatial analysis, machine learning).<BR>
This includes: <br>

##### Loading data

dea_tools.datahandling: Loading and handling DEA data (e.g. combining multiple products, handling CRSs, pansharpening)

##### Plotting and transforming data

dea_tools.plotting: Plotting DEA data (e.g. RGB plots, animations, interactive maps)
dea_tools.bandindices.py: Calculating remote sensing band indices (e.g. NDVI, NDWI)

##### Spatial and temporal analysis

dea_tools.spatial: Spatial analysis tools (e.g. rasterising, vectorising, contour extraction, image processing)
dea_tools.temporal: Temporal analysis tools (e.g. phenology, temporal statistics, multi-dimensional regression)

##### Classification and segmentation

dea_tools.classification.py: Machine learning classification (e.g. training and applying machine learning models on satellite data)
dea_tools.segmentation.py: Image segmentation tools (e.g. applying image segementation with RSGISLIB)

##### Parallel processing

dea_tools.dask: Parallel processing with Dask (e.g. creating Dask clusters for scalable analysis)

##### Domain-specific analysis

dea_tools.land_cover: Functions for plotting Digital Earth Australia Land Cover data.
dea_tools.coastal: Coastal and intertidal analysis tools (e.g. tidal tagging, coastal change timeseries)
dea_tools.bom: Loading Bureau of Meteorology water data service data (e.g. guage data, discharge data)
dea_tools.climate: Retrieving and manipulating gridded climate data (e.g. ERA5)
dea_tools.waterbodies: Loading and processing DEA Waterbodies data (e.g. finding and loading waterbody timeseries data)
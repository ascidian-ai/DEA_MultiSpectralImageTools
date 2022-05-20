# DEA Multi-Spectral Imaging Tools
#### Repo: https://github.com/ascidian-ai/DEA_MultiSpectralImageTools

Jupyter Notebooks and Python helper functions to support image extraction and preparation of Digital Earth Australia (DEA) Satellite Multi-Spectral Images for training a Deep Learning Model to predict land use classification.

Figure 1 below illustrates the data processing steps to generate an initial data stack covering a 50 x 25km surface of the Earth north of Adelaide, South Australia. 

Each 5,120m x 5,120m area tile contains a selection of Sentinel-2 satellite images taken during a particular time period and combined as different layers into a single xarray data stack that includes both visible(RGB) and Near Infrared (NIR) bands at 10m resolution.

After extraction of each set of satellite images, NDVI, NDWI and kNDVI indices are calculated and added as additional layers to each tile dataset.

Polygonal areas defining land use are then used to generate additional bitmask xarray layers for each tile and per land use type. In this project we are analysing crop types from the CLUMC dataset published by the Australian Department of Agriculture.

*Figure 1 : Example Data Processing Pipeline for Research Project*
<img src="_images/DataPipeline17May2022.svg" alt="Example Data Processing Pipeline for Research Project" width="800"/>
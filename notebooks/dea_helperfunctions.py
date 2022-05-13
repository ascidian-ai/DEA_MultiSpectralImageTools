import math
from datacube.utils.geometry import BoundingBox
from shapely.geometry import Polygon

class DEA_HelperFunctions:
    def __init__(self, earthradius=6371000, crs='EPSG:3577'):
        self.earthradius = earthradius # Radius of the Earth in metres
        self.crs = crs     # Coordinate Reference System, defaults here is EPSG:3577: GDA94 / Australian Albers projection
        
    def set_earthradius(self, earthradius):
        self.earthradius = earthradius
        return

    def set_crs(self, crs):
        self.crs = crs
        return
    
    
    ########################################################################################
    # Convert tile polygon to bounding box for use in odc stack queries
    #
    # origin are specified in the following order in degrees [ longitude, latitude ]
    # extent is specified in the following order [ horizontalextent(m), verticalextent(m)]
    # polygons is a list of polygons each defined by [min(lon), min(lat), max(lon), max(lat)]
    #          for its corresponding tile.
    #

    def convert_poly2bbox(self, polygon: Polygon) -> BoundingBox:
        return BoundingBox(polygon.bounds[0],polygon.bounds[1],polygon.bounds[2],polygon.bounds[3])
        
    ########################################################################################
    # Calculate tile polygons for entire area
    #
    # origin are specified in the following order in degrees [ longitude, latitude ]
    # extent is specified in the following order [ horizontalextent(m), verticalextent(m)]
    # polygons is a list of polygons each defined by [min(lon), min(lat), max(lon), max(lat)]
    #          for its corresponding tile.
    #

    def calc_surveyarea_polygons(self, origin=[0.0,0.0], tileresolution=[6400,4800], numtiles=[5,2]):
        polygons = [] # array of polygons representing each tile
        lons = [] # array of longitudes at the right of each tile
        lats = []  # array of latitudes at the top of each tile
        
        hbearing = math.radians(90) # bearing from true north for calculating 2nd longitude value
        vbearing = math.radians(0) # bearing from true north for calculating 2nd latitude value

        # add origin latitude & longitude in radians
        lons.append(math.radians(origin[0]))
        lats.append(math.radians(origin[1]))
        
        hd= tileresolution[0] # horizontal extent/distance in metres for each tile
        vd= tileresolution[1] # vertical extent/distance in metres for each tile
        
        for j in range(numtiles[1]): # iterate vertically
            newlat = math.asin( math.sin(lats[j])*math.cos(vd/self.earthradius)
                                 + math.cos(lats[j])*math.sin(vd/self.earthradius)*math.cos(vbearing))
            lats.append(newlat)
            
            for i in range(numtiles[0]): # iterate horizontally
                newlon = lons[i] + math.atan2(math.sin(hbearing)*math.sin(hd/self.earthradius)*math.cos(lats[j]),
                                         math.cos(hd/self.earthradius)-math.sin(lats[j])*math.sin(lats[j]))
                lons.append(newlon)
  
                polygon = Polygon([[math.degrees(lons[i]),math.degrees(lats[j])],
                                   [math.degrees(lons[i]),math.degrees(lats[j+1])],
                                   [math.degrees(lons[i+1]),math.degrees(lats[j+1])],
                                   [math.degrees(lons[i+1]),math.degrees(lats[j])]])
                polygons.append(polygon)
            
        return polygons
    
    ########################################################################################
    # Calculate bounding polygon for entire area
    #
    # origin are specified in the following order in degrees [ longitude, latitude ]
    # extent is specified in the following order [ horizontalextent(m), verticalextent(m)]
    # polygon returns [min(lon), min(lat), max(lon), max(lat)]
    #
    # Adapted from sourcecode located at
    # ref: https://stackoverflow.com/questions/7222382/get-lat-long-given-current-point-distance-and-bearing

    def calc_surveyarea_polygon(self, origin=[0.0,0.0], tileresolution=[1024,1024], numtiles=[1,1]):
        hbearing = math.radians(90) # bearing from true north for calculating 2nd longitude value
        vbearing = math.radians(0) # bearing from true north for calculating 2nd latitude value

        lat1 = origin[1]
        lon1 = origin[0]
        
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)

        hd= tileresolution[0]*numtiles[0] # horizontal extent/distance in metres
        vd= tileresolution[1]*numtiles[1] # vertical extent/distance in metres

        lat2_rad = math.asin( math.sin(lat1_rad)*math.cos(vd/self.earthradius)
                         + math.cos(lat1_rad)*math.sin(vd/self.earthradius)*math.cos(vbearing))

        lon2_rad = lon1_rad + math.atan2(math.sin(hbearing)*math.sin(hd/self.earthradius)*math.cos(lat1_rad),
                                 math.cos(hd/self.earthradius)-math.sin(lat1_rad)*math.sin(lat2_rad))

        lat2 = math.degrees(lat2_rad)
        lon2 = math.degrees(lon2_rad)
        
        polygon = Polygon([[lon1,lat1],[lon1,lat2],[lon2,lat2],[lon2,lat1]])
        
        return polygon
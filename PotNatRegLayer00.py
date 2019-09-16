#!/usr/bin/env python
"""
After that we should overlap this natural grasslands with ESA CCI 2000
agriculture and pasture and then
get covariables for the random points.
"""

import ee
import folium
from ee import batch
from pprint import pprint
# from IPython.display import Image
# import webbrowser

# init EE
ee.Initialize()

# Importing data
NaturalGrass = ee.Image("users/HotSpotRestoration/PotentialNaturalRegeneration/NatGrass1992");
CCI = ee.Image("users/HotSpotRestoration/ESACCI-LC-L4-LCCS-Map-300m-P1Y-1992_2015-v207");
elevation = ee.Image("USGS/SRTMGL1_003");
admin = ee.Image("CIESIN/GPWv411/GPW_Mean_Administrative_Unit_Area");

# Organizing data
CCI2000 = CCI.select(['b9'], ['PotRestArea00']); #Select landuse for year 2000
# Masking
CCI2000 = CCI2000.updateMask(elevation);

#masking landuses different than agriculture and grassland
CCI2000 = CCI2000.where(CCI2000.eq(0), 3);
CCI2000 = CCI2000.where(CCI2000.eq(10).And(CCI2000.eq(120)).And(CCI2000.eq(130)), 999)
#var CCI2000 = CCI2000.where(CCI2000.eq(10), 999);
#var CCI2000 = CCI2000.where(CCI2000.eq(20), 999);
#var CCI2000 = CCI2000.where(CCI2000.eq(130), 999);
CCI2000 = CCI2000.eq(999);
CCI2000 = CCI2000.mask(CCI2000);
pprint(CCI2000.getInfo());


# defyning global bound
coords = [[-180.0, -90.0], [180,  -90.0], [180, 90], [-180,90]]
globalGeo = ee.Geometry.Polygon(coords = coords, proj = ee.Projection( 'EPSG:4326' ), geodesic = False);

region = ([116.2621, 39.8412], [116.2621, 40.01236],[116.4849, 40.01236],[116.4849, 39.8412])

outCCI2000 = batch.Export.image.toAsset(\
  image = CCI2000,
  description = "PotRestArea00",
  #description: "Image from ESA CCI considering only pasture and grass land and disconsidering natural grasss land from IIS. pixel values = 1 considered areas for potential natural regeneration",
  assetId = "users/HotSpotRestoration/PotentialNaturalRegeneration/PotRestArea00",
  #pyramidingPolicy,
  #dimensions,
  region = coords,
  scale = 300,
  #crs,
  #crsTransform = [0.00833333333333333333, 0, -180, 0, -0.00833333333333333333, 90]
  maxPixels = 1e13
  )

process = batch.Task.start(outCCI2000)

outCCI2000.status()
pprint(batch.Task.status(outCCI2000))
"""
# Creating mapHack
class eeMapHack(object):
  def __init__(self, center=[0, 0], zoom=3):
    self._map = folium.Map(location=center, zoom_start=zoom)
    return

  def addToMap(self, img, vizParams, name):
    map_id = ee.Image(img.visualize(**vizParams)).getMapId()
    tile_url_template = "https://earthengine.googleapis.com/map/{mapid}/{{z}}/{{x}}/{{y}}?token={token}"
    mapurl = tile_url_template.format(**map_id)
    folium.WmsTileLayer(mapurl, name=name).add_to(self._map)
    return

  def addLayerControl(self):
    self._map.add_child(folium.map.LayerControl())
    return

# initialize map object
eeMap = eeMapHack(center=[18.453,-95.738],zoom=9)


# Define a method for displaying Earth Engine image tiles to folium map.
def add_ee_layer(self, eeImageObject, visParams, name):
  mapID = ee.Image(eeImageObject).getMapId(visParams)
  folium.raster_layers.TileLayer(
    tiles = "https://earthengine.googleapis.com/map/"+mapID['mapid']+
      "/{z}/{x}/{y}?token="+mapID['token'],
    attr = "Map Data © Google Earth Engine",
    name = name,
    overlay = True,
    control = True
  ).add_to(self)

# Add EE drawing method to folium.
folium.Map.add_ee_layer = add_ee_layer

# Set visualization parameters.
visParams = {'min':0, 'max':1, 'palette':['225ea8','41b6c4','a1dab4','ffffcc']}

# Create a folium map object.
myMap = folium.Map(location=[20, 0], zoom_start=3, height=500)

# Add the elevation model to the map object.
myMap.add_ee_layer(CCI2000, visParams, 'DEM')

# Add a layer control panel to the map.
myMap.add_child(folium.LayerControl())

# Display the map.
display(myMap)

#eeMap.addToMap(CCI2000, {}, 'CCI2000')
#eeMap.addToMap(CCI2000, {}, "Original");
# add layer control to map
#eeMap.addLayerControl()

#outHtml = 'map.html' # temporary file path, change if needed
#eeMap._map.save(outHtml)

#webbrowser.open('file://'+outHtml)
"""

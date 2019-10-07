#!/usr/bin/env python
"""
This script is organized to produce/identify areas for potential natural regeneration:
CCI ESA 2000 grass and agricultural lands, omitting natural grass lands layers on CCI ESA grassland class, which are not supposed to be restorable as they are natural grass lands).

Overlap this natural grasslands with ESA CCI 2000
agriculture and pasture

Latter by whatsapp:
Using NatGrass remove pixels that overlaps ESA2000 grasslands :. keeping only not natural grass lands which in deed was supposed to be restored.
Then, 'merge' with agriculture;
"""

import ee
from ee import batch
from pprint import pprint
import webbrowser
import folium

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

# init EE
ee.Initialize()

# Importing data
NaturalGrass = ee.Image("users/HotSpotRestoration/PotentialNaturalRegeneration/NatGrass1992")
CCI = ee.Image("users/HotSpotRestoration/ESACCI-LC-L4-LCCS-Map-300m-P1Y-1992_2015-v207")
elevation = ee.Image("USGS/SRTMGL1_003")
world = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")

# masking where there is Natural Grass pixels
NaturalGrassUnMask = NaturalGrass.unmask()
NaturalGrassInverted = NaturalGrassUnMask.eq(0)

# Organizing data
CCI2000 = CCI.select(['b9'], ['PotRestArea00']) #Select landuse for year 2000
# Masking
CCI2000 = CCI2000.updateMask(elevation)

#masking landuses different than agriculture and grassland
CCI2000 = CCI2000.where(CCI2000.eq(0), 3) # changing no data to other value so we dont have problem on masking
NatRegAreas = CCI2000.where(CCI2000.eq(10), 999)
NatRegAreas = NatRegAreas.where(NatRegAreas.eq(120), 999)
NatRegAreas = NatRegAreas.where(NatRegAreas.eq(130).And(NaturalGrassInverted), 999)
NatRegAreas = NatRegAreas.eq(999)
NatRegAreas = NatRegAreas.mask(NatRegAreas)

# print
pprint(NatGrassAnd.getInfo())
pprint(CCI2000.getInfo())

# Create a folium map object.
myMap = folium.Map(location=[-28, -46], zoom_start=6)

# Add the elevation model to the map object.
myMap.add_ee_layer(CCI2000, {'min':0, 'max':220, 'palette':['white','blue']}, 'CCI2000')
myMap.add_ee_layer(NatRegAreas, {'min':0, 'max':1, 'palette':['red','black']}, 'NatRegAreas')
myMap.add_ee_layer(NaturalGrass.mask(NaturalGrass), {'min':0, 'max':1, 'palette':['green','yellow']}, 'NaturalGrass')

# Add a layer control panel to the map.
myMap.add_child(folium.LayerControl())
# Display the map.
myMap.save("my_map.html")
webbrowser.open('./my_map.html')

# defyning global bound
coords = [[-180.0, -90.0], [180,  -90.0], [180, 90], [-180,90]]

# process tasks
outNatRegAreas = batch.Export.image.toAsset(\
  image = NatRegAreas,
  description = "PotRestArea00",
  #description: "Image from ESA CCI considering only pasture and grass land and disconsidering natural grasss land from IIS. pixel values = 1 considered areas for potential natural regeneration",
  assetId = "users/HotSpotRestoration/PotentialNaturalRegeneration/PotRestArea00",
  #pyramidingPolicy,
  #dimensions,
  region = coords,
  scale = 300,
  #crs = 'EPSG:4326',
  #crsTransform = crs_transform,
  maxPixels = 1e13
  )

process = batch.Task.start(outNatRegAreas)

# checking task status
outNatRegAreas.status()
pprint(batch.Task.status(outNatRegAreas))

import ee
from pprint import pprint

# init EE
ee.Initialize()

# Importing data
#potAreas = ee.Image("users/HotSpotRestoration/PotentialNaturalRegeneration/PotRestArea00")
world = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")
pprint(world.limit(1).getInfo()["features"][0]["properties"]["wld_rgn"])
for i in world:
    pprint(i.getInfo())


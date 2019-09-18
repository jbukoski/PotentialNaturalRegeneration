import ee
import webbrowser
from pprint import pprint

# init EE
ee.Initialize()

# Importing data
potAreas = ee.Image("users/HotSpotRestoration/PotentialNaturalRegeneration/PotRestArea00") # https://code.earthengine.google.com/?asset=users/HotSpotRestoration/PotentialNaturalRegeneration/PotRestArea00
world = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")

# Create a folium map object.
myMap = folium.Map(location=[-28, -46], zoom_start=6)

# Add the elevation model to the map object.
myMap.add_ee_layer(potAreas, {'min':0, 'max':1, 'palette':['white','blue']}, 'potAreas')
#myMap.add_ee_layer(world, {}, 'world')

# Add a layer control panel to the map.
myMap.add_child(folium.LayerControl())
# Display the map.
myMap.save("../my_map.html")
webbrowser.open('../my_map.html')

randomPoints = potAreas.sample(region = world.limit(1), scale = 300,
                               #projection, factor,
                               numPixels = 2,
                               seed = 1#, dropNulls, tileScale, geometries
)
pprint(randomPoints.getInfo())

# creating function to sample based on fc
def sample(fc):
    tempPotArea = potAreas.clip(fc)
    rndmPts = tempPotArea.sample(region = fc.geometry(),
                                 scale = 300,
                                 #projection, factor,
                                 numPixels = 2,
                                 seed = 1,
                                 dropNulls = True,
                                 tileScale = 16,
                                 geometries = True
                                 )
    return rndmPts

# testing
worldLimited = world.limit(3)
testeFunc = sample(worldLimited)
pprint(testeFunc.getInfo())

# testing w/ map
testeMapFunc = worldLimited.map(sample)
pprint(testeMapFunc.getInfo())
#r = testeMapFunc.getInfo()
#pprint(r.keys())
#pprint(r['features'])
#pprint(r['properties'])




pprint(testeMapFunc.toGeoJSONString())
unioned = testeMapFunc.union()
pprint(unioned.getInfo())
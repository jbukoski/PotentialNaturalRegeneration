import ee
from ee import batch
import webbrowser
from pprint import pprint

# init EE
ee.Initialize()

# Importing data
potAreas = ee.Image("users/HotSpotRestoration/PotentialNaturalRegeneration/PotRestArea00")
world = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")

vecpotareas = potAreas.reduceToVectors(#reducer = ee.Reducer.first(),
                                                 geometry = world,
                                                                     scale =  300,
                                                                              #'geometryType', eightConnected, labelProperty, crs, crsTransform,
                                                                              bestEffort = True,
#maxPixels,
tileScale = 8 #, geometryInNativeProjection
)

# process tasks
outvecpotareas = batch.Export.table.toAsset(\
    collection = vecpotareas,
    description = "teste description",
    assetId = "users/HotSpotRestoration/PotentialNaturalRegeneration/vecpotareas00")

process = batch.Task.start(outvecpotareas)

# checking task status
outvecpotareas.status()
pprint(batch.Task.status(outvecpotareas))

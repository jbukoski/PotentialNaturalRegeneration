import ee
from ee import batch
import webbrowser
from pprint import pprint

# init EE
ee.Initialize()

# Importing data
potAreas = ee.Image("users/HotSpotRestoration/PotentialNaturalRegeneration/PotRestArea00")
world = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")

table = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_2")
table2 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_3")
table3 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_4")
table4 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_5")
table5 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_6")
table6 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_7")
table7 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_8")

# change the geometry to each table
vecpotareas3_2 = potAreas.reduceToVectors(geometry = table.geometry().bounds(),
                                          scale =  300,
                                          bestEffort = True,
                                          tileScale = 8)
vecpotareas3_3 = potAreas.reduceToVectors(geometry = table2.geometry().bounds(),
                                          scale =  300,
                                          bestEffort = True,
                                          tileScale = 8)
vecpotareas3_4 = potAreas.reduceToVectors(geometry = table3.geometry().bounds(),
                                          scale =  300,
                                          bestEffort = True,
                                          tileScale = 8)
vecpotareas3_5 = potAreas.reduceToVectors(geometry = table4.geometry().bounds(),
                                          scale =  300,
                                          bestEffort = True,
                                          tileScale = 8)
vecpotareas3_6 = potAreas.reduceToVectors(geometry = table5.geometry().bounds(),
                                          scale =  300,
                                          bestEffort = True,
                                          tileScale = 8)
vecpotareas3_7 = potAreas.reduceToVectors(geometry = table6.geometry().bounds(),
                                          scale =  300,
                                          bestEffort = True,
                                          tileScale = 8)
vecpotareas3_8 = potAreas.reduceToVectors(geometry = table7.geometry().bounds(),
                                          scale =  300,
                                          bestEffort = True,
                                          tileScale = 8)


# process Output tasks
outvecpotareas2 = batch.Export.table.toAsset(\
    collection = vecpotareas3_2,
    description = "",
    assetId = "users/HotSpotRestoration/PotentialNaturalRegeneration/vecpotareas00_3_2")
outvecpotareas3 = batch.Export.table.toAsset(\
    collection = vecpotareas3_3,
    description = "",
    assetId = "users/HotSpotRestoration/PotentialNaturalRegeneration/vecpotareas00_3_3")
outvecpotareas4 = batch.Export.table.toAsset(\
    collection = vecpotareas3_4,
    description = "",
    assetId = "users/HotSpotRestoration/PotentialNaturalRegeneration/vecpotareas00_3_4")
outvecpotareas5 = batch.Export.table.toAsset(\
    collection = vecpotareas3_5,
    description = "",
    assetId = "users/HotSpotRestoration/PotentialNaturalRegeneration/vecpotareas00_3_5")
outvecpotareas6 = batch.Export.table.toAsset(\
    collection = vecpotareas3_6,
    description = "",
    assetId = "users/HotSpotRestoration/PotentialNaturalRegeneration/vecpotareas00_3_6")
outvecpotareas7 = batch.Export.table.toAsset(\
    collection = vecpotareas3_7,
    description = "",
    assetId = "users/HotSpotRestoration/PotentialNaturalRegeneration/vecpotareas00_3_7")
outvecpotareas8 = batch.Export.table.toAsset(\
    collection = vecpotareas3_8,
    description = "",
    assetId = "users/HotSpotRestoration/PotentialNaturalRegeneration/vecpotareas00_3_8")

process3_2 = batch.Task.start(outvecpotareas2)
process3_3 = batch.Task.start(outvecpotareas3)
process3_4 = batch.Task.start(outvecpotareas4)
process3_5 = batch.Task.start(outvecpotareas5)
process3_6 = batch.Task.start(outvecpotareas6)
process3_7 = batch.Task.start(outvecpotareas7)

# checking task status
#outvecpotareas.status()
#pprint(batch.Task.status(outvecpotareas))
outvecpotareas2.status()
outvecpotareas3.status()
outvecpotareas4.status()
outvecpotareas5.status()
outvecpotareas6.status()
outvecpotareas7.status()
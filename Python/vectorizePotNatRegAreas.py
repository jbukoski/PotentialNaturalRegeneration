import ee
from ee import batch
import webbrowser
from pprint import pprint

# init EE
ee.Initialize()

# Importing data
potAreas = ee.Image("users/HotSpotRestoration/PotentialNaturalRegeneration/PotRestArea00")
world = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")

NatGrass1992
PotRestArea00
PredRF_Finv9_mergeArea_v9pass3_2
PredRF_Finv9_mergeArea_v9pass3_3
PredRF_Finv9_mergeArea_v9pass3_4
PredRF_Finv9_mergeArea_v9pass3_5
PredRF_Finv9_mergeArea_v9pass3_6
PredRF_Finv9_mergeArea_v9pass3_7
PredRF_Finv9_mergeArea_v9pass3_8
RegenerationRaster
random_regen
CropPastures
ESACCI-LC-L4-LCCS-Map-300m-P1Y-1992_2015-v207
ESACCI-LC-L4-LCCS-Map-300m-P1Y-2015-v207
ESAUrbanArea
ESAUrbanArea2
GlobalForestClasification
GovernanceF32_pxl
GovernancePolygon
HumanFootPrint
IDH
RuralPopDistribution
RuralPovertyDensity
Soil_CEC_1km
VALIDATION_stats2ndRound
grip4_total_dens_m_km2
grip4_tp1_dens_m_km2
grip4_tp2_dens_m_km2
grip4_tp3_dens_m_km2
grip4_tp4_dens_m_km2
grip4_tp5_dens_m_km2
landuse2015_300m_WGS84
opportunity_costs_comb_900m_Molweide_WGS84
soil_BLDFIE_30cm_1km
soil_PHIHOX_30cm_1km
soil_PHIKCL_30cm_1km
soil_SNDPPT_30cm_1km
New Script *

Use print(...) to write to this console.

table = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_2")
table2 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_3")
table3 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_4")
table4 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_5")
table5 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_6")
table6 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_7")
table7 = ee.FeatureCollection("users/HotSpotRestoration/PotentialNaturalRegeneration/PredRF_Finv9_mergeArea_v9pass3_8")


vecpotareas = potAreas.reduceToVectors(#reducer = ee.Reducer.first(),
                                                 geometry = table.geometry().bounds(),
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

# Potential for natural regeneration
About emojis:  
:black_square_button: confirm something of the following sentence;  
:question: define how to solve the following issue/sentence;  
:heavy_check_mark: Question/point already defined;  

## General overview:  
This modeling and study is different form the previous. We do not have study coordinates, we have pixels were natural regeneration occurred across the study area. He (Matt Fagan) calculated natural regeneration between 2000 and 2012 using the Hansen data - including loss and gain. So, the original data is for 2000, the last data is for 2012 and regeneration occurred in 12 years.  
Current scenario: Analysis done from 2000 to 2015, but regeneration up to 2012;  

[For more information, see project's overwiew](https://trello.com/c/LPu48ZNL)  

## Layers:  
* [Natural regeneration (2000-2012);](#Matts-data)  
* [Potential Natural Regeneration Areas at 2000;](#Potential-Natural-Regeneration-Areas)  
* [Natural grass land;](#About-Strassburgs-natural-grassland-layer)  
* [Potential Natural Regeneration Areas at 2000 **that didn't regenerated**;](#Potential-Natural-Regeneration-Areas-Not-Regenerated)  
* [Covariate layers;](#About-covariate-layers)  
* [No Restorable Areas;](#No-Restorable-Areas)  
* ["Actual" Potential Natural Regeneration Areas;](#Actual-Potential-Natural-Regeneration-Areas)  

### Matt's data:  
the original forest cover for Hansen is for the year 2000.  
The gain pixels were reclassified into two groups:  
* plantations (timber or tree crops);
* natural regeneration (delta 2000-2012);  
**Obs**: all standing in 2015, for at least three years  

> Also yes, it does not represent the total gain in forest cover in 2015, as other areas may have appears 2013-2015.  (Fagan)  

* The Fagan data provides the mask for the areas that regenerated forest.  

### Potential Natural Regeneration Layer  
This layer was produced by using ESA CCI land cover for year 2000; We considered as potential for natural regeneration land cover all classes related with grassland and agriculture. For more info: [see ESA CCI legend](https://github.com/FelipeSBarros/PotentialNaturalRegeneration/blob/master/CCI_Legend.md) or [layer creation script - GEE Python API](./Python/PotNatRegLayer.py).  
From the classes mentioned above, we removed pixels identified as natural grassland ([**Strassburg et al. under review**](#About-Strassburgs-natural-grassland-layer)), as we don't espect natural grass areas to be forested.  
This is used to generate the non-regeneration random points  
> **These can just be binary rasters** if that is easiest.  

#### About Strassburg's natural grassland layer:  

>"As the ESA CCI map does not distinguish cultivated from natural grasslands, we 
used the Terrestrial Ecoregions of the World and the Gridded Livestock of the World 
datasets to classify each pixel into natural (not needing restoration) or cultivated grasslands 
(potentially restorable pasturelands). If a pixel classified as grasslands (class 130) in the ESA-CCI 
is located within an Ecoregion of non-grassland ecosystems (e.g. forests), and if it presents a cattle 
density equal or higher than 1 head/km-2, it was reclassified to “pasturelands”, otherwise it was 
reclassified to “native grassland”."

### Potential Natural Regeneration Layer [**that Not Regenerated**]  
Ideally this would be done at the same resolution as the Fagan data and would meet these criteria:
        1. if a cell is "1" in the Fagan data (i.e. it regenerated), it cannot also be part of this set (i.e. obviously a cell cannot be coded as both regenerating and not regenerating).  
        1. it must have been non-forest at the beginning of the time-series  
        1. it should exclude all cells that were never forest, or that have no possibility of being forest (i.e. all urban/developed areas, water, wetlands, etc)  
        1. the cell must fall within the spatial domain defined above  


### No Restorable Areas  
* Urban areas (CCI ESA Urban Areas); 
* wetlands  
* water bodies  
* natural grassland (Strassburg et al.)  
1. On Pablo's paper: we mask (exclude):
    * Water body;  
    * Wetlands;
    * Permanent snow and ice area (Oslon data. If necessary [take a look here](https://github.com/FelipeSBarros/WorldRestorationUncertainty#updating-forested-areas-2017)  

### Actual Potential Natural Regeneration Areas  
For prediction purpose  
> **These can just be binary rasters** if that is easiest.  
  
1. Restorable areas from "Global restoration opportunities in tropical
rainforest landscapes": [GEE code here](https://code.earthengine.google.com/46c209046cecd3349e5b36eed5de67e3)  
>""We estimated the persistence chances of restored
forests using the relative rate of recent tree cover loss as surrogate.
To do so, we summed forest cover loss from 2001 to 2015 and di-
vided it by forest cover in 2000, using data from (48). We applied
a threshold of 20% tree canopy cover for year 2000 data to produce
a binary map of forest (1)/nonforest (0) on its original spatial resolution
(fig. S8C)." ("Global restoration opportunities in tropical
rainforest landscapes")  

## Felipe tasks
- [ ] **layers organization**  
    - [X] [ESA CCI data](http://maps.elie.ucl.ac.be/CCI/viewer/): Download and upload as GEE asset ESA CCI land use and cover data for 2000 and 2015;  
    - [X] [Natual grassland layer](#About-Strassburgs-natural-grassland-layer): upload as asset;
    - [X] Create [Potentia Natural Regeneration Layer](#Potential-Natural-Regeneration-Areas) as asset;  
    - [ ] Look for layers about River;    
    - [ ] Generate random points on Potential Natural Regeneration Areas;  
    - [ ] Build distance layers (GEE algorithms [~~option I~~](https://developers.google.com/earth-engine/api_docs#eeimagedistance) ~~or~~ [option II](https://developers.google.com/earth-engine/api_docs#eeimagefastDistanceTransform)) for:  
        - [ ] [Hansen] forest at a 30m resolution and would need to be done at two time periods:
            - [ ] 2000 and;  
            - [ ] if distance to forest is included in the final model (it probably will be) we also need distance to current forest for the predictive modelling - so perhaps **based on the most recent Hansen data**;  
        - [ ] urban areas (ESA CCI distace at a 300m resolution);  
        - [ ] rivers;  
- [ ] Organize/produce ([covariate](#About-covariate-layers)) data  
- [ ] Extract data (covariate values) considering:  
    - [X] the radius defined/discussed on [About layers](#About-covariate-layers);  
    - [X] point based;  
    - [Script](https://code.earthengine.google.com/a6ccffd4bc98f44cb3da3efba61693d0)
- [X] Felipe, I have sent you other potential data, can you review your e mails to check if you can get  and process it.  
*Couldn't get the orignal data. asked Pablo to help.*    
- [X] ~~Felipe, attached the supplementary material for the AF study. There you can find all variables we used and the buffer sizes as well (I think so)~~.  
    **After contact on Whatsapp: past disturbance intensity is just for Brazil... we won't use. (28/07/2019)**;    

### Pablo's tasks
1. Pablo, can you write here the methodology we used for your current paper.
1. Help with layers used on Nanni et. al. ("The neotropical reforestation hotspots: A biophysical and socioeconomic typology of contemporary forest expansion"):  
    * "Rural-urban ratio", 
    * "Rural Population Change" and 
    * "Urban Population Change";  

## About analysis process  
For the pixel scale analysis we will want to do this:  
1. generate sample points from the Fagan regeneration areas;  
1. generate sample points representing the [:checkbox:] areas that could have regenerated over the same time interval but did not. [point defined on item 2.1 of Boundary for the spatial domain](#boundary-for-the-spatial-domain);  
1. for all the points in 1 & 2, acquire covariate data for each of those coordinates from the various datasets you have compiled (distance to forest, elevation, etc). [**Link to the covariate table**](https://www.dropbox.com/s/10nd7y6yk2y97ef/Environmental%20and%20socioeconomic%20variables_19_07_08.xlsx?dl=0);  
1. use the data from steps 1-3 to create models predicting regeneration potential (will be done by **Hawthorne**);  
1. :heavy_check_mark: apply those models back to each of the cells in which regeneration is possible ( :black_square_button: not sure if we have defined that set yet, but it is probably going to be all the pasture and agriculture cells, therefore excluding other natural habitats like grasslands, and water, urban, etc);   
~~:heavy_check_mark: ~~**landuse according to IIS layer?**;~~  
Yes, starting 2015 CCI data converted to 30m excluding natural; landuse cover from CCI;  
1. we then need to perform various summaries of that prediction raster;  

**Hawthorne**:  leading 4;   
**Felipe**: leading 1-3, 5 and 6;  

### Alternatives processes:  
* **Converting the Fagan data to raster** is certainly an option and we will probably need to do it anyway to integrate that data into whatever land cover data we are using.  
    * :heavy_check_mark: **But if** the conversion to raster and the random point generation with those rasters is **problematic then we can devise ways of processing the polygon data to do the random sampling (weighted probability sampling of polygons by area of polygon and then random point generation within each polygon)**. **This was done and is documented on [sampling.r](./R/sampling.r)**.  
* Start sampling exercise to understand its procedure; Should we be concerned with NA? I was expecting that would be possible to inform a raster stack instead of polygons and by doing this only the pixels with value would be sample. But I'm not sure if this is possible.  

### Boundary for the spatial domain  
1. The Fagan polygons seem to cover the band of latitudes from +25 to -25, excluding temperate forest data keeping only humid tropical forests.   
    :heavy_chack_mark: ~~Should we focuss **in tropical and subtropical forest ecosystems** (the same boundary for the Pablo's paper in the current CIFOR project).~~  
    > I have been thinking about whether to use the ecoregions boundaries to define the spatial domain, and I am now thinking that we should not do that. The trouble with the ecoregions is that they are mapped at a very coarse mapping resolution. Of course there is a great deal of variation in habitat within each of those ecoregions and some of the ecoregions classified as non-forest at a coarse scale may contain regions of forest within them. Our analysis uses data with a much finer mapping resolution. So, for now, I suggest we treat our spatial domain as: all terrestrial land between 25 to -30 latitude (or whatever the exact latitude extent of the Fagan data is).  

## About covariate layers  

### About buffers  
1.1. Buffers. I have changed all buffers to 2 km. For forest data we will do it buffers for ~~500m, 1 km and~~ 2 km (accorded by e-mail [25 de set de 2019] that focal window will be done on 2 Km only ). I removed buffer needs for data with coarse resolution, for example 10 km.  
1.2. Red color. I used to show lkayers taht we should not use because we have it in a better resolution.  
1.3. Orange color. I used to show layers taht we may want to produce using differnet years or range of years.  
1.4. Yellow color. I used to include variables that we will need build distance layers. For example distance to forest. I included it only. Which are the others I should include (Hawthorne): distance to rivers, roads, urban areas, forestry and natural regeneration?  

The only datasets I think would be useful to run as focal datasets are:  

1. Cropland and pasture at 329 m resolution with a 2 km buffer to calculation proportion of cropland.  
    * CropII - :heavy_check_mark:  
    * PastureIIS - :heavy_check_mark:  
    **Note that if we use a 1 km buffer, that is only 29 cells falling within the window. The problem with that is that there are then only 29 unique values possible in the response variable, which makes it more similar to a categorical variable in the context of random forest modelling. A 2km buffer would have 113 cells so 113 possible values, so that makes it more like a continuous variable. As a general rule of thumb, it might be best to avoid using a buffer size that results in less than 50 cells (and preferably more like 100) in the window to avoid the limited unique value problem.**

1. Cropland at 30 m resolution with a 2 km buffer :heavy_check_mark:  
1. Gross deforestation at 30 m resolutions with a 2 km buffer :heavy_check_mark:
1. Human population at 250 m resolution with a 2 km buffer :heavy_check_mark:  
1. Strictly Protected Area at 1 km  with a 2 km buffer :heavy_check_mark:  
1. Sustainable Protected Area at 1 km with a 2 km buffer :heavy_check_mark:  
1. Urban area at 300 m reslution with a 2 km buffer :heavy_check_mark:  
1. Slope at 30m resolution with a 500 m buffer :heavy_check_mark:  
1. - [ ] Forest cover (one date near the beginning of the time series) at a 30m resolution with a 500 m, 1 km and 2 km buffer.   
1. Human Footprint Index (To be defined if buffer moving window or as point-based);  

### Points-based:  
1. the identify of the country/territory within which the pixel falls [~~GADM~~](https://gadm.org/data.html) [actually using LISB](http://geonode.state.gov/) :heavy_check_mark:  
1. the identify of the biome, ecoregion and province within which the pixel falls. Most current data from Ecorregions (2017), originally from Olson.  
1. :heavy_check_mark: the identity of the continent within which the pixel falls. **Not necessary, anymore. Only ecoregion;**  
1. the lat and lon of each point :heavy_check_mark: **Yes, inform lat/long**;  
1. does the pixel fall within a protected area? (And perhaps the type of protected area, if the global protected area dataset has multiple levels that might be related to forest regeneration. For example, some times of protected status may still allow some level of forestry). https://www.protectedplanet.net/ (:heavy_check_mark: **Yes, inform the PA's cathegory**;  
1. Elevation: I don't think we need a focal window, just use the pixel value. :heavy_check_mark:  
1. Althought it is ambigous, I produced both, point based and on buffer analysis: **Slope I did not include a buffer because we want the information at the point with natural regeneration or without natural regeneration, so we need the data at the point only.** :heavy_check_mark:  

**Some other points**
* the scale of the focal window size: 2km radius range (accorded by e-mail [25 de set de 2019])  

## About Scripts:  
* [PotNarRegLayer](./Python/PotNatRegLayer.py): GEE Python API to identify areas that, on year 2000, had potential was availible for natural regeneration. Using 2000 CCI ESA specific land use classes ([see legend](./CCI_Legend.md)) for more info), pixels identifyed as Natural Grass (Layer from Strassburg et al.) were excluded. Result are saved as image GEE asset;  
* [PotNatRegSamplePoints](./Python/PotNatRegSamplePoints.py): GEE Python API script to, based on **PotNatRegLayer**, generate [550,000 random points](Discussions on clases and definitons) that will be used to get covariate data. **Script not finilized**;  
* [vectorizePotNatRegAreas](./Python/vectorizePotNatRegAreas.py): GEE Python API to convert PotNatRegLayer on featureCollection to, later, generate random points based on each feature area. **Vectorization is done splitting data in different bounding box. Sampling points not done**";  

### Discussions on clases and definitons

1. :heavy_check_mark: Do you already have an algorithm for generating random points and what is it? How feasible **would it be to generate 550,000 random points in the regeneration areas (regen=1)**; and **550,000 in the non-regeneration areas (regen=0)**? That would be **1.1 million in total**, but we would expect to lose some of those to NoData problems when intersecting with the covariate datasets, hence we might end up with approximately 1 million. **This was done and is documented on [sampling.r](./R/sampling.r)**.  
    1. **I need you to tell me what sorts of numbers are realistic if this is asking too much.** One of the reasons I am asking for a lot is that we will almost certainly want to run some country-level or continental-level models to evaluate whether this improves prediction accuracy, so we need to make sure we have enough sample points within each of those strata.  
    * Ultimately we need to generate two sets of random points:
        * 500,000 points representing a random sample of cells that regenerated (the Fagan mask) - as described above 
        * 500,000 points representing a random sample of cells that did not regenerate (the other mask defined above).  
They can be combined into a dataset has the x and y coordinates, and a field called "regen" that is coded as a "1" for all the cells that regenerated, and a "0" for all the cells that did not. So that dataset will be 1 million records in length. However, if 500,000 is going to take far too long, then start with 100,000.

> we need to be able to describe a rational approach to buffer selection that passes peer review. Some common approaches used are: (i) select a constant buffer size and argue that is the focal area that is likely to affect regeneration potential in a given cell; (ii) select a different buffer size for groups of variables (environmental, biological, socioeconomic) and justify the buffer size for each of those three groups; (iii) justify a buffer size for each dataset individually; (iv) assume that all variables may be relevent at multiple scales and summarise the variables at site (~30m), local (~1km) and regional (~10km) scales. It seems to be (iii) that is the current strategy, which is fine but harder work to justify each buffer size. I wonder if a radius larger than 10 km perhaps becomes harder to link to forest regeneration within a cell?  

> This is an important general point: we are building a statistical model of forest regeneration over the last 20 years for which we want predictor variables that relate to conditions near the start of that period. But for predicting future regeneration we want to use variables representing current conditions. Many of the variables will not change for various reasons, but key ones related to forest cover and distance to forest should be calculated separately for each of those two time periods whenever possible.

## GEE Python API environment setting  

```
conda create -n PotNatRegProj python  
conda activate PotNatRegProj  
conda install -c conda-forge earthengine-api  
earthengine authenticate  
pip install -U folium, ipython , jupyter 
```  
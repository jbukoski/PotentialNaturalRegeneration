# Potential for natural regeneration
About emojis:  
:black_square_button: confirm something of the following sentence;  
:question: define how to solve the following issue/sentence;  
:heavy_check_mark: Question/point already defined;  

## General overview:  
This modeling and study is different form the previous. We do not have study coordinates, we have pixels were natural regeneration occurred across the study area. He (Matt Fagan) calculated natural regeneration between 2000 and 2012 using the Hansen data - including loss and gain. So, the original data is for 2000, the last data is for 2012 and regeneration occurred in 12 years.  
:black_square_button: If we want to use the most actual forest cover map we could build it to 2017, but from 2012 to 2017 we have data on forest loss only - not gain. So, maybe 2012 will be our "current" scenario. I will check these informations with Matt. :question: **This need to be confirmed**   

[For more information, see project's overwiew](https://trello.com/c/LPu48ZNL)  

### Matt's data:
the original forest cover for Hansen is for the year 2000.  
The gain pixels were reclassified into two groups:  

    * plantations (timber or tree crops);
    * natural regeneration (delta 2000-2012);
**Obs**: all standing in 2015, for at least three years
       
> Also yes, it does not represent the total gain in forest cover in 2015, as other areas may have appears 2013-2015.  (Fagan)


### Felipe tasks
- [ ] [layers organization](https://code.earthengine.google.com/a6ccffd4bc98f44cb3da3efba61693d0)  
    - [ ] Build distance to nearest forest at a 30m resolution and would need to be done at two time periods [see ](#questions-i-believe-been-answered).
    - [ ] Felipe produce the new layers we will need - layers based on distance and with other years.
        - [ ] for the current modelling we need distance to forest near to the beginning of our time period (not sure what time period the Fagan data spans - is it ~~1995~~ 2000-2015?). **Aclaration** see [Matt's data section for more infor about time range](#matts-data);  
        - [ ] if distance to forest is included in the final model (it probably will be) we also need distance to current forest for the predictive modelling - so perhaps based on the most recent Hansen data;
    - [ ] Felipe produce data in the buffer sizes we discussed and extract data for mean at the country or county level.  
    - [ ] Felipe start to extract data in the ~~stratified~~ random sample that we have discussed with Hathorne.  
    - [ ] Look for layers about River;  
 
- [X] Felipe, you should include the data that we have information for layers that we have comments in orange and it will help us to define the year we will use (or window) for each layer. The first thing is to have this table full and ready to be used.  
- [X] share with Hawthorne how we defined retorable ([see 11th point of "About layers" section](#about-layers))/non-restorable ([see 10th point of "About layers" section](#about-layers)) areas;  
- [X] Felipe, I have sent you other potential data, can you review your e mails to check if you can get  and process it.   
    Couldn't get the orignal data. asked Pablo to help.  
- [X] Organize the data mentioned on [Som other points](#points-based)  
- [X] ~~Felipe, attached the supplementary material for the AF study. There you can find all variables we used and the buffer sizes as well (I think so)~~.  
    **After contact on Whatsapp: past disturbance intensity is just for Brazil... we won't use. (28/07/2019)**;    
- [X] Converted the Fagan polygons to raster; [for more info see rasterizationProcess.md](./rasterizationProcess.md)  

- [ ] Regeneration data validation: [for more info see valiationProcess.md](./validationProcess.md);  

- [X] ~~Check how feasably would be generating 1.1 milion points. [More info on "Questions I believe been answered"](#questions-i-believe-been-answered). First atempt [here](https://code.earthengine.google.com/6ed68da4bfc03a4bb14126294555848d);~~ Random sample points were done and is documented on [sampling.r](./R/sampling.r).
- [ ] Check if Hawthorne concern about getting NA/NoData values is needed or we could avoid it somehow, reduzing number of points to be generated;    
       
- [ ] It would be better to start with a more constrained problem. It would be ideal to take on the modelling for one of the biomes in Brazil because we already have a modelling framework that works quite well for the **AF** and could be readily adapted to other biomes. But I will write up the modelling process in detail for this global analysis and we can talk through it.

**To keep in mind**  
> Felipe, it would be good to report/record any processing that ends up modifying the units, if that ever happens (e.g. I sometimes do things like multiply by a constant and then convert to integer to save on disk space, but that could change units).

### Pablo's tasks
1. Pablo, can you write here the methodology we used for your current paper.
1. Help with layers used on Nanni et. al. ("The neotropical reforestation hotspots: A biophysical and socioeconomic typology of contemporary forest expansion"):  
    * "Rural-urban ratio", 
    * "Rural Population Change" and 
    * "Urban Population Change";  

### About analysis process  
For the pixel scale analysis we will want to do this:  
1. generate sample points from the Fagan regeneration areas;  
1. generate sample points representing the [:cehckbox:] areas that could have regenerated over the same time interval but did not. [point defined on item 2.1 of Boundary for the spatial domain](#boundary-for-the-spatial-domain);  
1. for all the points in 1 & 2, acquire covariate data for each of those coordinates from the various datasets you have compiled (distance to forest, elevation, etc). [**Link to the covariate table**](https://www.dropbox.com/s/10nd7y6yk2y97ef/Environmental%20and%20socioeconomic%20variables_19_07_08.xlsx?dl=0);  
1. use the data from steps 1-3 to create models predicting regeneration potential (will be done by **Hawthorne**);  
1. apply those models back to each of the cells in which regeneration is possible ( :black_square_button: not sure if we have defined that set yet, but it is probably going to be all the pasture and agriculture cells, therefore excluding other natural habitats like grasslands, and water, urban, etc);  
:question: **landuse according to IIS layer?**;  
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
1. Within that overall spatial domain, **we will also need to define the areas that**:  
    1. :black_square_button: were available for forest regeneration 20 years ago (or at the beginning of the Fagan time-series) (this is used to generate the non-regeneration random points); :heavy_exclamation_mark: ([see 1st and 2nd points of About Layes section](#about-layers) **These can just be binary rasters** if that is easiest.  
    1. I think **we do not want stratified random sampling** at this time. :heavy_check_mark: Let's try the random sampling functionality in GEE and see how it goes.  **This was done and is documented on [sampling.r](./R/sampling.r)**.
    1. :black_square_button: We also need a definition of 'available for regeneration': That would include agriculture and pasture for sure.
    1. :black_square_button: We also need a definition of non-potentially restorable: Urban, water, wetlands, native grasslands, etc; ([see 10th point of "About layers" section](#about-layers))  
    1. :black_square_button: that are available for forest regeneration now (this is used for the predictions); :heavy_exclamation_mark:**These can just be binary rasters** if that is easiest.  
    1. :black_square_button: It would be good to discuss with Hawthorne as well which year would be the best to measure forest cover; **[This seems to have already defined/solved on  Matt's data section](#matts-data)**. **Could anyone confirm?**  
    1.  :question: how to measure restorable and non-restorable areas.([see 10/11th point of "About layers" section](#about-layers))  
    1. :black_square_button: we need to decide what will be our "current" scenario and the best data for using in each variable as they may have different data of updates.  

* Question from Hawthorne:
    1. Are you OK with exlucding Deserts & Xeric grasslands?  
    1. Do we include Flooded Grasslands & Savannahs so that the Pantanal is included in the analysis?  
    1.  Which option would you argue for:  
        - Include all Montane Grasslands & Shrublands? 
        - Include only African Montane Grasslands & Shrublands? 
        - Exclude all Montane Grasslands & Shrublands?
    1. OK to include Tropical & Subtropical coniferous forest?  
    1. :heavy_check_mark: The other two ecoregions are extensive and have lots of forest regeneration within them, so are included for sure:  
        - Tropical & Subtropical Dry Broadleaf Forests  
        - Tropical & Subtropical Moist Broadleaf Forests  
* Tropical & Subtropical coniferous forest, Tropical & Subtropical Dry Broadleaf Forests, Tropical & Subtropical Moist Broadleaf Forests. That is, critical areas such as - Tropical & Subtropical Grasslands, Savannas & Shrublands - should not be included in my point of view. Reasons: 1) our study is focused exclusively in forest biomes (even for TRENDS) and Fagan's work as well, 2) these delimitations are too course and it may also has affected Fagan's data. But we should be conservative, I would prefer to avoid any risk of including afforestation in our map, 3) our contract is for (humid) forests, we are doing more than this and it is great.  I only would like to include (sub-)tropical forests of Australia, they don't have it in the ecorregions and we have some data there. Do you have any shapefile for it Hawthorne?  

### About layers

* The Fagan data provides the mask for the areas that regenerated forest.  
* The other mask we need to develop is **the areas that could have regenerated but did not**. Ideally this would be done at the same resolution as the Fagan data and would meet these criteria:
    1. (i) if a cell is "1" in the Fagan data (i.e. it regenerated), it cannot also be part of this set (i.e. obviously a cell cannot be coded as both regenerating and not regenerating).
    1. (ii) it must have been non-forest at the beginning of the time-series
    1. (iii) it should exclude all cells that were never forest, or that have no possibility of being forest (i.e. all urban/developed areas, water, wetlands, etc)
    1. (iv) the cell must fall within the spatial domain defined above
>If this cannot be done at the same resolution as the Fagan data, OK, let's just proceed with it at whatever best resolution we can.

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
**I note those two variables could be added together in R to obtain total protected area, so no need to calculate that as part of the geoprocessing.**  
:question: **I dind't understand the sentence above.**  
1. Urban area at 300 m reslution with a 2 km buffer :heavy_check_mark:  
1. Slope at 30m resolution with a 500 m buffer :heavy_check_mark:  
1. - [ ] Forest cover (one date near the beginning of the time series) at a 30m resolution with a 500 m, 1 km and 2 km buffer.  
**~~Note that Forest cover is one of the few variables where we need to explore multiple radii. I see there are several forest cover datasets at 30 m so we may need to discuss which one to use.~~** Defined on "so perhaps based on the most recent Hansen data" statement.  

#### Points-based:  
1. the identify of the country/territory within which the pixel falls [~~GADM~~](https://gadm.org/data.html) [actually using LISB](http://geonode.state.gov/) :heavy_check_mark:  
1. the identify of the biome, ecoregion and province within which the pixel falls. Most current data from Ecorregions (2017), originally from Olson.  
1. the identity of the continent within which the pixel falls. :question:  
1. the lat and lon of each point :question: ;  
1. does the pixel fall within a protected area? (And perhaps the type of protected area, if the global protected area dataset has multiple levels that might be related to forest regeneration. For example, some times of protected status may still allow some level of forestry). https://www.protectedplanet.net/ (:question: **How should I ideintify protection type? by category? 0/1?**) :heavy_protected_area:  
1. Elevation: I don't think we need a focal window, just use the pixel value. :heavy_check_mark:  
1. Althought it is ambigous, I produced both, point based and on buffer analysis: **Slope I did not include a buffer because we want the information at the point with natural regeneration or without natural regeneration, so we need the data at the point only.** :heavy_check_mark:  

**Some other points**
* the scale of the focal window size: it will be somewhere in the 0.5-2km radius range (yet to be determined exactly). :heavy_check_mark:  

1. Non-restorable areas:  
    On Pablo's paper: we mask (exclude):
    * Water body;  
    * Wetlands;
    * Permanent snow and ice area (Oslon data. If necessary [take a look here](https://github.com/FelipeSBarros/WorldRestorationUncertainty#updating-forested-areas-2017)  
    * ~~Hansen's masked areas~~;
    * ~~Hansen's forest areas w/ 100% fo forest cover~~;

1. Restorable areas: [GEE code here](https://code.earthengine.google.com/46c209046cecd3349e5b36eed5de67e3) 
    >""We estimated the persistence chances of restored
forests using the relative rate of recent tree cover loss as surrogate.
To do so, we summed forest cover loss from 2001 to 2015 and di-
vided it by forest cover in 2000, using data from (48). We applied
a threshold of 20% tree canopy cover for year 2000 data to produce
a binary map of forest (1)/nonforest (0) on its original spatial resolution
(fig. S8C)." (Global restoration opportunities in tropical
rainforest landscapes")  
    * :black_square_button: To use the same [Restorable areas] map from the global prioritization (Bernardo's paper).
    * :black_square_button: Check if we could use data from this new paper in Science.


### About buffers  
1.1. Buffers. I have changed all buffers to 2 km. For forest data we will do it buffers for 500m, 1 km and 2 km. I removed buffer needs for data with coarse resolution, for example 10 km. 

1.2. Red color. I used to show lkayers taht we should not use because we have it in a better resolution.

1.3. Orange color. I used to show layers taht we may want to produce using differnet years or range of years.

1.4. Yellow color. I used to include variables that we will need build distance layers. For example distance to forest. I included it only. Which are the others I should include (Hawthorne): distance to rivers, roads, urban areas, forestry and natural regeneration?

### Discussions on clases and definitons

1. :black_square_button: Are there any ambiguous land use categories we need to discuss? How can we develop these two datasets?  

1. **Confirmar com renatinho**: Felipe has developed this layer already for us, right? (**Which paper?**) Can you remember me as we developed it - ESA CCI? At lower resolution (30 m) we have some more detailed layers that we could try to build this potentially restorable areas more detailed. In summary, this is a key point and before starting to get the data we need to have clear which database we will use to build it. ([see 11th point of "About layers" section](#about-layers))    

1. :heavy_check_mark: Do you already have an algorithm for generating random points and what is it? How feasible **would it be to generate 550,000 random points in the regeneration areas (regen=1)**; and **550,000 in the non-regeneration areas (regen=0)**? That would be **1.1 million in total**, but we would expect to lose some of those to NoData problems when intersecting with the covariate datasets, hence we might end up with approximately 1 million. **This was done and is documented on [sampling.r](./R/sampling.r)**.  
    1. **I need you to tell me what sorts of numbers are realistic if this is asking too much.** One of the reasons I am asking for a lot is that we will almost certainly want to run some country-level or continental-level models to evaluate whether this improves prediction accuracy, so we need to make sure we have enough sample points within each of those strata.  
    * Ultimately we need to generate two sets of random points:
        * 500,000 points representing a random sample of cells that regenerated (the Fagan mask) - as described above 
        * 500,000 points representing a random sample of cells that did not regenerate (the other mask defined above).  
They can be combined into a dataset has the x and y coordinates, and a field called "regen" that is coded as a "1" for all the cells that regenerated, and a "0" for all the cells that did not. So that dataset will be 1 million records in length. However, if 500,000 is going to take far too long, then start with 100,000.

> we need to be able to describe a rational approach to buffer selection that passes peer review. Some common approaches used are: (i) select a constant buffer size and argue that is the focal area that is likely to affect regeneration potential in a given cell; (ii) select a different buffer size for groups of variables (environmental, biological, socioeconomic) and justify the buffer size for each of those three groups; (iii) justify a buffer size for each dataset individually; (iv) assume that all variables may be relevent at multiple scales and summarise the variables at site (~30m), local (~1km) and regional (~10km) scales. It seems to be (iii) that is the current strategy, which is fine but harder work to justify each buffer size. I wonder if a radius larger than 10 km perhaps becomes harder to link to forest regeneration within a cell?  

> This is an important general point: we are building a statistical model of forest regeneration over the last 20 years for which we want predictor variables that relate to conditions near the start of that period. But for predicting future regeneration we want to use variables representing current conditions. Many of the variables will not change for various reasons, but key ones related to forest cover and distance to forest should be calculated separately for each of those two time periods whenever possible.

### Questions I believe been answered

1. :heavy_check_mark: Do the Fagan polygons already exclude forestry?  
    Answer: I saw that they classifyied as plantation and regrowth, also take a look on [Matt's data section](#matts-data);  
1. There is no "distance to nearest forest" variable. I see you say we can extract them. I care most about distance to forest, and am less concerned about including distance to roads or rivers. I think distance to forest should be calculated at a 30m resolution and would need to be done at two time periods:  
    Answer: OK, already done in Felipe'staks section; 
1. :black_square_button: Felipe, when we start to use this data I would like to check if we have information for natural regeneration and plantation only or forest cover as well. Otherwise we will need to generate foret cover data from Hansen for 2000 and 2012.
    Answer: I believe this is already defined. But not sure. **Could someone confirm?**
1. check if we have information for natural regeneration and plantation only or forest cover as well. Otherwise we will need to generate foret cover data from Hansen for 2000 and 2012.  
    Answer: This seems to be solved, right?  **Could someone confirm?**

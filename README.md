# Potential for natural regeneration

[For more information, see prject's overwiew](https://trello.com/c/LPu48ZNL)  

Felipe, this modeling and study now is different form the previous. We do not have study coordinates, we have pixels were natural regeneration occurred across the study area. He (Matt Fagan) calculated natural regeneration between 2000 and 2012 using the Hansen data - including loss and gain. So, the original data is for 2000, the last data is for 2012 and regeneration occurred in 12 years. If we want to use the most actual forest cover map we could build it to 2017, but from 2012 to 2017 we have data on forest loss only - not gain. So, maybe 2012 will be our "current" scenario. I will check these informations with Matt.  

For the pixel scale analysis we will want to do this:  
1. generate sample points from the Fagan regeneration areas;  
1. generate sample points representing the areas that could have regenerated over the same time interval but did not;  
:question: **How to identify then?**  
1. for all the points in 1&2, acquire covariate data for each of those coordinates from the various datasets you have compiled (distance to forest, elevation, etc). [**Link to the covariate table**]();  
1. use the data from steps 1-3 to create models predicting regeneration potential [**Hawthorne**];  
1. apply those models back to each of the cells in which regeneration is possible (not sure if we have defined that set yet, but it is probably going to be all the pasture and agriculture cells, therefore excluding other natural habitats like grasslands, and water, urban, etc);  
:question: **landuse according to IIS layer?**;  
1. we then need to perform various summaries of that prediction raster;  

**Hawthorne**:  leading 4;   
**Felipe**: leading 1-3, 5 and 6;  

## Details and questions of the analysis:

**Boundary for the spatial domain**  
1. The Fagan polygons seem to cover the band of latitudes from +25 to -25 (I think), excluding temperate forest data keeping only humid tropical forests. **Focusing in tropical and subtropical forest ecosystems** (the same boundary for the Pablo's paper in the current CIFOR project).   

1. Within that overall spatial domain, **we will also need to define the areas that**:  
    1. were available for forest regeneration 20 years ago (or at the beginning of the Fagan time-series) (this is used to generate the non-regeneration random points);  
    1.  I think **we do not want stratified random sampling** at this time. Let's try the random sampling functionality in GEE and see how it goes.  
    1. that are available for forest regeneration now (this is used for the predictions);  
    1. We also need a definition of 'available for regeneration': That would include agriculture and pasture for sure.  
    1. We also need a definition of non-potentially restorable: Urban, water, wetlands, native grasslands, etc;  
    1,  It would be good to discuss with Hawthorne as well which year would be the best to measure forest cover.  
    1.  how to measure restorable and non-restorable areas.  
    1. I wonder if we should be including more country-level socioeconomic data?  
    1. we need to decide what will be our "current" scenario and the best data for using in each variable as they may have different data of updates.  



**These can just be binary rasters** if that is easiest. 

Are there any ambiguous land use categories we need to discuss? How can we develop these two datasets?  

**Confirmar com renatinho**: Felipe has developed this layer already for us, right? (**Which paper?**) Can you remember me as we developed it - ESA CCI? At lower resolution (30 m) we have some more detailed layers that we could try to build this potentially restorable areas more detailed. In summary, this is a key point and before starting to get the data we need to have clear which database we will use to build it.  

    1. Do the Fagan polygons already exclude forestry?  
**I saw that they classifyied as plantation and regrowth;**  

    1. Do you already have an algorithm for generating random points and what is it? How feasible **would it be to generate 550,000 random points in the regeneration areas (regen=1)**; and **550,000 in the non-regeneration areas (regen=0)**? That would be **1.1 million in total**, but we would expect to lose some of those to NoData problems when intersecting with the covariate datasets, hence we might end up with approximately 1 million.  
    1. **I need you to tell me what sorts of numbers are realistic if this is asking too much.** One of the reasons I am asking for a lot is that we will almost certainly want to run some country-level or continental-level models to evaluate whether this improves prediction accuracy, so we need to make sure we have enough sample points within each of those strata.  

* It would be better to start with a more constrained problem. It would be ideal to take on the modelling for one of the biomes in Brazil because we already have a modelling framework that works quite well for the AF and could be readily adapted to other biomes. But I will write up the modelling process in detail for this global analysis and we can talk through it. **How could we go thru it?**

## Alternatives processes:  
* **Converting the Fagan data to raster** is certainly an option and we will probably need to do it anyway to integrate that data into whatever land cover data we are using.  
    * **But if** the conversion to raster and the random point generation with those rasters is **problematic then we can devise ways of processing the polygon data to do the random sampling (weighted probability sampling of polygons by area of polygon and then random point generation within each polygon)**.  
* Start sampling exercise to understand its procedure; Should we be concerned with NA? I was expecting that would be possible to inform a raster stack instead of polygons and by doing this only the pixels with value would be sample. But I'm not sure if this is possible.  

:question:3- Felipe, I have sent you other potential data, can you review your e mails to check if you can get  and process it. **Is it the same we used to Luí analysis?**  

* take a look on layer about River  
    * Felipe, attached the supplementary material for the AF study. There you can find all variables we used and the buffer sizes as well (I think so).  
    * the scale of the focal window size: it will be somewhere in the 0.5-2km radius range (yet to be determined exactly).  
* share with Hawthorn how we defined retorable/non-restorable areas;  
    * Restorable areas - we have, at least, four ways to do it:
      1. Pablo, can you write here the methodology we used for your current paper.
      1. Try to build agriculture, pasturelands, road, urban areas, forest (natural regeneration and etc) at the lowest resolution to build it.
      1.To use the same map from the global prioritization (Bernardo's paper).
      1.Check if we could use data from this new paper in Science.  

* There is no "distance to nearest forest" variable. I see you say we can extract them. I care most about distance to forest, and am less concerned about including distance to roads or rivers. I think distance to forest should be calculated at a 30m resolution and would need to be done at two time periods:  
    1. for the current modelling we need distance to forest near to the beginning of our time period (not sure what time period the Fagan data spans - is it ~1995-2015?);  
    1. if distance to forest is included in the final model (it probably will be) we also need distance to current forest for the predictive modelling - so perhaps based on the most recent Hansen data?  

## Layers 
The only datasets I think would be useful to run as focal datasets are:

(1) Cropland and pasture at 329 m resolution with a 2 km buffer to calculation proportion of cropland.

Note that if we use a 1 km buffer, that is only 29 cells falling within the window. The problem with that is that there are then only 29 unique values possible in the response variable, which makes it more similar to a categorical variable in the context of random forest modelling. A 2km buffer would have 113 cells so 113 possible values, so that makes it more like a continuous variable. As a general rule of thumb, it might be best to avoid using a buffer size that results in less than 50 cells (and preferably more like 100) in the window to avoid the limited unique value problem.

(2) Cropland at 30 m resolution with a 2 km buffer

(3) Gross deforestation at 30 m resolutions with a 2 km buffer

(4) Human population at 250 m resolution with a 2 km buffer

Assuming that the resolutions of these two datasets:
Strictly Protected Area
Sustainable Protected Area
are actually 111.3 m, not 111.3 km (is that a typo?), then:

(5) Strictly Protected Area at 111.3 m with a 2 km buffer
(6) Sustainable Protected Area at 111.3 m with a 2 km buffer

I note those two variables could be added together in R to obtain total protected area, so no need to calculate that as part of the geoprocessing.

(7) Urban area at 300 m reslution with a 2 km buffer

(8) Forest cover (one date near the beginning of the time series) at a 30m resolution with a 500 m, 1 km and 2 km buffer. Note that Forest cover is one of the few variables where we need to explore multiple radii. I see there are several forest cover datasets at 30 m so we may need to discuss which one to use.

Elevation: I don't think we need a focal window, just use the pixel value.

(9) Slope at 30m resolution with a 500 m buffer?


I think all the rest of the variables we could process as pixel data (no focal windows).
What do you think?


1.1. Buffers. I have changed all buffers to 2 km. For forest data we will do it buffers for 500m, 1 km and 2 km. I removed buffer needs for data with coarse resolution, for example 10 km. Slope I did not include a buffer because we want the information at the point with natural regeneration or without natural regeneration, so we need the data at the point only. This was my thinking to tell which variables we need buffer or not.

1.2. Red color. I used to show lkayers taht we should not use because we have it in a better resolution.

1.3. Orange color. I used to show layers taht we may want to produce using differnet years or range of years.

1.4. Yellow color. I used to include variables that we will need build distance layers. For example distance to forest. I included it only. Which are the others I should include (Hawthorne): distance to rivers, roads, urban areas, forestry and natural regeneration?

1.5. Protected areas. I think it is in metter and not km as I wrote. I changed to metters - Pablo, can you check it please.


2.1. Felipe and Hawthorne. Can you check it please? Hawthorne, you should say if you are ok with thew information in the excel. Felipe, you should include the data that we have information for layers that we have comments in orange and it will help us to define the year we will use (or window) for each layer. The first thing is to have this table full and ready to be used.

2.2. Felipe produce the new layers we will need - layers based on distance and with other years.

2.3. Felipe produce data in the buffer sizes we discussed and extract data for mean at the country or county level - Hawthorne, you need to suggest here.

2.4. Felipe start to extract data in the stratified sample that we have discussed with Hathorne.

Am I correct here? Didi I miss something? Hawthorne, it is likely taht Felipe will can star t to work on these data this week. But let's have this table finished first. I think he will be quick on it based on previous data he has been developed.

3- News:
Just to make clear Matt told me that his data is the delta from 2000 to 2012 but standing in 2015. So, I assume we have forest cover in 2012, natural regeneration and forestry that occurred from 2000 to 2012, but all these three classes standing in 2015 (a criterion).


the original forest cover for Hansen is for the year 2000.  I just reclassified the gain pixels into two groups: plantations (timber or tree crops) and natural regeneration (delta 2000-2012).  And yes, all standing in 2015, so these two classes had to stand for at least three years.  Not ideal, but that was the limit of the data we had.  Also yes, it does not represent the total gain in forest cover in 2015, as other areas may have appears 2013-2015.  


Felipe, when we start to use this data I would like to check if we have information for natural regeneration and plantation only or forest cover as well. Otherwise we will need to generate foret cover data from Hansen for 2000 and 2012.


### Points-based:  
* the identify of the country/territory within which the pixel falls [GADM](https://gadm.org/data.html)  
* the identify of the biome, ecoregion and province within which the pixel falls. Most current data from Ecorregions (2017), originally from Olson.  
* the identity of the continent within which the pixel falls. :question:  
* the lat and lon of each point;  
* does the pixel fall within a protected area? (And perhaps the type of protected area, if the global protected area dataset has multiple levels that might be related to forest regeneration. For example, some times of protected status may still allow some level of forestry). https://www.protectedplanet.net/ (**How should I ideintify protection type? by category? 0/1?**)  

:warning: And Felipe, it would be good to report/record any processing that ends up modifying the units, if that ever happens (e.g. I sometimes do things like multiply by a constant and then convert to integer to save on disk space, but that could change units).  

> we need to be able to describe a rational approach to buffer selection that passes peer review. Some common approaches used are: (i) select a constant buffer size and argue that is the focal area that is likely to affect regeneration potential in a given cell; (ii) select a different buffer size for groups of variables (environmental, biological, socioeconomic) and justify the buffer size for each of those three groups; (iii) justify a buffer size for each dataset individually; (iv) assume that all variables may be relevent at multiple scales and summarise the variables at site (~30m), local (~1km) and regional (~10km) scales. It seems to be (iii) that is the current strategy, which is fine but harder work to justify each buffer size. I wonder if a radius larger than 10 km perhaps becomes harder to link to forest regeneration within a cell?  

> This is an important general point: we are building a statistical model of forest regeneration over the last 20 years for which we want predictor variables that relate to conditions near the start of that period. But for predicting future regeneration we want to use variables representing current conditions. Many of the variables will not change for various reasons, but key ones related to forest cover and distance to forest should be calculated separately for each of those two time periods whenever possible.

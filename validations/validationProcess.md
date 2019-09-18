# Validation process of regrowth data

This is a report of validation process requested by Hawthorne. You can find more information on [Felipe's tasks on README document](./README.md/#felipe-tasks):  

* [Validation process started here](https://code.earthengine.google.com/c37db48ed353a44a4aee0d5f12c13869);

**It would be useful to confirm that it meets the criteria that:**  
- [X] (i) the Fagan polygons were non-forest at the beginning of the time series.  
- [ ] (ii) the polygons have been forested for at least the last 3 consecutive years in the time series  
- [ ] (iii) the polygons are part of a regiongroup region that is at least 5 cells, allowing connections on the diagonal.  
> If you have the ability to look at that data and see if my interpretation seems correct that would be good. If any of those criteria have not been met we will need to think about whether we want to do them ourselves or adjust the details of the analysis that we did for the AF.

## Validation process
All fagan's regrowth data were uploaded to GEE, them in the validation script, those data were used together with hansen's `treecover2000`, `loss` and `lossyear`.  
To get a better overview of all data ~~about 1000 polygons were randomly sampled~~ and had `treecover`, `loss` and `lossyear` extracted to compute a histogram.  
![tree cover at 2000](./img/TreeCover2000.png)  
![forest loss in the time range](./img/loss.png)  

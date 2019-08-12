
# Hawthorne Beyer

# purpose: generate completely random sample of points falling within polygons from 
# a polygon shapefile or set of polygon shapefiles.

# requires an area field in the shapefile table

# this needs to be run a macine with enough RAM to load these big shapefiles into R
# or R will crash - at least 20GB?

# personal notes:
# rclone copy --include *.zip --drive-shared-with-me 'google:Matt Fagan Tree Plantation Classification (v0.8)' ./


# infiles <- c("./rf_6/PredRF_Finv9_mergeArea_v9pass3_6", 
# "./rf_8/PredRF_Finv9_mergeArea_v9pass3_8", 
# "./rf_3/PredRF_Finv9_mergeArea_v9pass3_3", 
# "./rf_2/PredRF_Finv9_mergeArea_v9pass3_2", 
# "./rf_7/PredRF_Finv9_mergeArea_v9pass3_7", 
# "./rf_4/PredRF_Finv9_mergeArea_v9pass3_4", 
# "./rf_5/PredRF_Finv9_mergeArea_v9pass3_5")

# or this, depending on how you unzipped the files
infiles <- c("PredRF_Finv9_mergeArea_v9pass3_6", 
"PredRF_Finv9_mergeArea_v9pass3_8", 
"PredRF_Finv9_mergeArea_v9pass3_3", 
"PredRF_Finv9_mergeArea_v9pass3_2", 
"PredRF_Finv9_mergeArea_v9pass3_7", 
"PredRF_Finv9_mergeArea_v9pass3_4", 
"PredRF_Finv9_mergeArea_v9pass3_5")

areafld <- "shparea"


# get the areas:
library(foreign)

pareas <- c()
n <- rep(0, length(infiles))

for (i in 1:length(infiles)){
	data <- read.dbf(paste0(infiles[i], ".dbf"))
	n[i] <- dim(data)[1]
	pareas <- c(pareas, data[,areafld])
}
rm(data)
pcumrec <- c(0, cumsum(n))
index <- c(1:length(pareas))

# sample polygons in proportion to area
samp1 <- sample(index, 5E5, replace=TRUE, prob=pareas)

# order those samples:
samp1 <- sort(samp1)

# now generate the spatial points:
library(raster)
require(rgdal)
sfidxcurr <- 0
sf <- NULL

# load the required function
generate.random.point <- function(poly){
	while(TRUE){
		rx <- runif(10, poly@bbox[1,1], poly@bbox[1,2])
		ry <- runif(10, poly@bbox[2,1], poly@bbox[2,2])
		sp <- SpatialPoints(cbind(rx, ry), proj4string=CRS(projection(sf)))
		spin <- sp[poly,]
		if (length(spin) > 0) return(coordinates(spin)[1,])	
	}
}


Sys.time()
rndxy <- matrix(0, nrow=length(samp1), ncol=2)
for (i in 1:length(samp1)){
	if (i %% 10000 == 0) message(i)
	sfidx <- max(which(pcumrec <= samp1[i]))
	if (sfidx != sfidxcurr){
		# load shapefile
		rm(sf)
		gc()
		# use the first one of these if all the shapefiles are in separate folders:
		#sf <- readOGR(dsn = substr(infiles[sfidx], 1, 6), layer = substr(infiles[sfidx], 8, nchar(infiles[sfidx])))
		sf <- readOGR(dsn = ".", layer = infiles[sfidx])
		sfidxcurr <- sfidx
	}

	rec <- samp1[i] - pcumrec[sfidx]
	# poly <- sf[rec,]
	rndxy[i,] <- generate.random.point(sf[rec,])
}
Sys.time()


rnd.df <- data.frame(rndxy, rep(1, length(samp1)), pareas[samp1])
colnames(rnd.df) <- c("x", "y", "regen", "polyarea")

save(rnd.df, file="rnd.df.RData")

# write as point shapefile:
coordinates(rnd.df) <- ~x+y
proj4string(rnd.df) <- projection(sf)
writeOGR(rnd.df, dsn=".", layer="random_regen", driver="ESRI Shapefile")



# scp 10.161.135.10:~/DATA/hbeyer/proj/cifor/random_regen.tar.gz .
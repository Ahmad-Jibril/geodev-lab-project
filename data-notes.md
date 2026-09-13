# Data notes

## Lagos LGA Boundary

1. How many rows?
20 features, representing the 20 Local Government Areas (LGAs) of Lagos State.


2. What are the column names?
fid, id, amapcode, editor, globalid, lgacode, lganame, source, statecode, statename, timestamp, uniq_id, and geometry.


3. What type is each column?
The dataset contains integer/identifier fields, text fields, a timestamp field, and polygon geometry. The geometry is MultiPolygon.


4. Are there nulls?
The important identification fields required for the analysis were checked and are populated. We should still retain the original data and let the database validation catch any non-critical nulls.


5. What geometry type?
MultiPolygon.


6. Does the coverage look complete?
Yes. The layer represents the 20 LGAs of Lagos State and provides the administrative framework for our LGA-level analysis.


## GRID3 Settlement Data

1. How many rows?
The cleaned GRID3 dataset contains the settlement/building-block features downloaded for the Lagos study area. Use the feature count shown in your cleaned layer, because the earlier count referred to the original downloaded data before the final cleaning.


2. What are the column names?

fid
block_id
country
iso3
block_area_sqm
block_perimeter
block_neighbor_count
building_count
building_area_min
building_area_max
building_area_sum
building_area_median
building_area_stdev
building_area_percentage
extent_type
mgrs_code
ndvi_mean
evi_mean
gbuilding_max_height
gbuilding_mean_height
blocks_per_settl_extent
building_count_density_quantile_rank
building_max_area_quantile_rank
building_count_density
bd_class
ma_class
composite_class
layer
path


3. What type is each column?
The layer contains integer fields, numeric fields for areas, densities and building measurements, text fields for identifiers/classes, and polygon geometry.


4. Are there nulls?
The important fields required for our analysis were checked during cleaning. We also verified the block_id values. The apparent duplicate block_id issue was caused by the data being loaded three times, not by duplicate blocks in the actual GRID3 dataset.


5. What geometry type?
Polygon/MultiPolygon settlement-block geometry, standardized to MultiPolygon for the PostGIS workflow.


6. Does the coverage look complete?
Yes for the downloaded Lagos study area. The layer provides contemporary built-environment/settlement coverage that we will use as supporting information and recent-period validation/context.

## WorldPop 2020 — nga_ppp_2020

1. How many rows?
11,546 raster rows.


2. What are the column names?
Raster datasets don't have normal attribute-table columns. It is a single-band population raster.


3. What type is each column?
The raster contains numeric population values representing the number of people per grid cell.


4. Are there nulls?
The raster uses -99999 as the NoData value. These cells must be excluded when calculating population statistics.


5. What geometry type?
Raster. Resolution is approximately 100 m.


6. Does the coverage look complete?
Yes. The dataset covers Nigeria and therefore completely encompasses the Lagos study area.

## WorldPop 2024 — nga_pop_2024

1. How many rows?
11,539 raster rows.


2. What are the column names?
It is a single-band population raster rather than a conventional vector attribute table.


3. What type is each column?
Numeric population-count values representing the estimated population within each grid cell.


4. Are there nulls?
The raster uses -99999 as NoData, which must be excluded from population calculations.


5. What geometry type?
Raster, with approximately 100 m spatial resolution.


6. Does the coverage look complete?
Yes. The Nigeria-wide dataset covers the entire Lagos study area.

## Landsat 1985

1. How many rows?
1,672 raster rows.


2. What are the column names?
Six reflective bands:

SR_B1
SR_B2
SR_B3
SR_B4
SR_B5
SR_B7


3. What type is each column?
Numeric raster bands containing surface-reflectance values.


4. Are there nulls?
No explicit NoData value was reported in the exported raster metadata. We will nevertheless check for invalid pixels during preprocessing.


5. What geometry type?
Raster, approximately 30 m resolution.


6. Does the coverage look complete?
Yes. The exported 1985 composite covers the Lagos study area without the earlier coverage problem we encountered.

## Landsat 2000

1. How many rows?
1,672 raster rows.


2. What are the column names?

SR_B1
SR_B2
SR_B3
SR_B4
SR_B5
SR_B7


3. What type is each column?
Numeric surface-reflectance raster bands.


4. Are there nulls?
No explicit NoData value was reported. Invalid pixels will be checked during preprocessing.


5. What geometry type?
Raster, approximately 30 m resolution.


6. Does the coverage look complete?
Yes. The composite covers the study area.

## Landsat 2010

1. How many rows?
1,672 raster rows.


2. What are the column names?

SR_B1
SR_B2
SR_B3
SR_B4
SR_B5
SR_B7


3. What type is each column?
Numeric surface-reflectance raster bands.


4. Are there nulls?
No explicit NoData value was reported. Invalid pixels will be checked during preprocessing.


5. What geometry type?
Raster, approximately 30 m resolution.


6. Does the coverage look complete?
Yes. The composite covers the Lagos study area.

## Landsat 2020

1. How many rows?
1,672 raster rows.


2. What are the column names?

SR_B2
SR_B3
SR_B4
SR_B5
SR_B6
SR_B7


3. What type is each column?
Numeric surface-reflectance raster bands.


4. Are there nulls?
No explicit NoData value was reported. Invalid pixels will be checked during preprocessing.


5. What geometry type?
Raster, approximately 30 m resolution.


6. Does the coverage look complete?
Yes. The composite covers the study area.

## Landsat 2025

1. How many rows?
1,672 raster rows.


2. What are the column names?

SR_B2
SR_B3
SR_B4
SR_B5
SR_B6
SR_B7


3. What type is each column?
Numeric surface-reflectance raster bands.


4. Are there nulls?
No explicit NoData value was reported. Invalid pixels will be checked during preprocessing.


5. What geometry type?
Raster, approximately 30 m resolution.


6. Does the coverage look complete?
Yes. The composite covers the Lagos study area.

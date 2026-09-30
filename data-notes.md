# Data Notes

**Week 2 Deliverables.** GeoDev Lab Africa Cohort 1.

**Author:** *Ahmad Jibril-Adeyemi*

---

``
What I downloaded, where it came from, what is in it, and what is wrong with it.
``

## Summary

| S/N | Dataset | Type | Retrieved | Status |
|---|---|---|---|---|
|1 | Lagos State LGA Boundaries | Vector | Yes | Good |
|2 | FABDEM (Bare Earth Elevation) | Raster | Yes | Good |
|3 | Lagos Drainage Network & Canal | Vector | Yes | Good |
|4 | Google Open Buildings V3 | Vector | Yes | Good |
|5 | Motorable Roads | Vector | Yes | Good |
|6 | Land Use Data | Raster | Yes | Good |
|7 | Soil Composition Grids | Raster | Yes | Good |
|8 | Rainfall Data | Raster | Yes | Good |
|9 | Public & Institutional Land | Vector | Yes | Good|
|10 | Protected Ecological Reserves | Vector | Yes | Good |
|11 | Sentinel-1 Satellite Imagery | Vector | Yes | Good |

## 1. Lagos LGA Boundary

- **Source:** HDX Nigeria
- **Retrieved:** Yes
- **File:** `data/raw/Lagos State LGA boundary`
- **Format:** GeoPackage
- **Geometry Type:** Polygon (MultiPolygon)
- **Feature Count:** 20
- **CRS as Downloaded:** EPSG:4326 - WGS 84

## Key Columns

| Column | What it Entails | Nulls |
|---|---|---|
|`admin1_name` | States the state name | Nil |
|`admin2_name` | States the LGA name | Nil |
|`fid` | The identifier | Nil |

**What I noticed**

> - Some of the LGA polygons cover the water bodies
> - Part of the Lagoon is already cut out (i.e it has no *polygon* feature)

## 2. FABDEM (Bare Earth Elevation Data)

- **Source:** Awesome GEE Community Catalog through Google Earth Engine (GDAL)
- **Retrieved:** Yes
- **File:** `data/raw/Lagos_BareEarth_FABDEM_30m`
- **Format:** GeoTIFF
- **Geometry Type:** Raster
- **Feature Count:** 1 band
- **CRS as Downloaded:** EPSG:4326 - WGS 84 - Geographic

## 3. Lagos Drainage Network & Canal

- **Source:** Open Street Map through QGIS (Ogr)
- **Retrieved:** Yes
- **File:** `data/raw/Lagos_Drainage_Canals_Network`
- **Format:** GeoPackage 
- **Geometry Type:** Line (MultiLineString)
- **Feature Count:** 1047
- **CRS as Downloaded:** EPSG:4326 - WGS 84

## Key Columns

| Column | What it Entails | Nulls |
|---|---|---|
|`waterway` | What type of network is it (i.e Is it a drain or a canal) | Nil |
|`name` | The name of the Drainage/Canal | 1003 |
| `tunnel` | description | 736 |

**What I noticed**

> The datasets takes longer than required to load sometimes

## 4. Google Open Buildings 

- **Source:** Google-Microsoft Open Buildings
- **Retrieved:** Yes but as a Parquet file which was converted to a `*.gpkg*` file
- **File:** `data/raw/Lagos_Google_Open_Buildings`
- **Format:** GeoPackage
- **Geometry Type:** Polygon (MultiPolygon)
- **Feature Count:** 2682816
- **CRS as Downloaded:** EPSG:4326 - WGS 84

## Key Columns

| Column | What it Entails | Nulls |
|---|---|---|
|`fid` | The identifier | Nil |
|`confidence` | The confidence level for the validity of each building  | Nil |
|`area_in_meters` | description | Nil |

## 5. Motorable Roads

- **Source:** 
- **Retrieved:**
- **File:** `data/raw/filename`
- **Format:**
- **Geometry Type:**
- **Feature Count:**
- **CRS as Downloaded:**

## Key Columns

| Column | What it Entails | Nulls |
|---|---|---|
|`column 1` | description | count |
|`column 2` | description | count |
|`column 3` | description | count |

**What I noticed**

> Gaps, duplcates, odd values, name spelling that differ from your other datasets

## 6.

- **Source:**
- **Retrieved:**
- **File:** `data/raw/filename`
- **Format:**
- **Geometry Type:**
- **Feature Count:**
- **CRS as Downloaded:**

## Key Columns

| Column | What it Entails | Nulls |
|---|---|---|
|`column 1` | description | count |
|`column 2` | description | count |
|`column 3` | description | count |

**What I noticed**

> Gaps, duplcates, odd values, name spelling that differ from your other datasets

## 7.

- **Source:**
- **Retrieved:**
- **File:** `data/raw/filename`
- **Format:**
- **Geometry Type:**
- **Feature Count:**
- **CRS as Downloaded:**

## Key Columns

| Column | What it Entails | Nulls |
|---|---|---|
|`column 1` | description | count |
|`column 2` | description | count |
|`column 3` | description | count |

**What I noticed**

> Gaps, duplcates, odd values, name spelling that differ from your other datasets

## 8.

- **Source:**
- **Retrieved:**
- **File:** `data/raw/filename`
- **Format:**
- **Geometry Type:**
- **Feature Count:**
- **CRS as Downloaded:**

## Key Columns

| Column | What it Entails | Nulls |
|---|---|---|
|`column 1` | description | count |
|`column 2` | description | count |
|`column 3` | description | count |

**What I noticed**

> Gaps, duplcates, odd values, name spelling that differ from your other datasets

## 9.

- **Source:**
- **Retrieved:**
- **File:** `data/raw/filename`
- **Format:**
- **Geometry Type:**
- **Feature Count:**
- **CRS as Downloaded:**

## Key Columns

| Column | What it Entails | Nulls |
|---|---|---|
|`column 1` | description | count |
|`column 2` | description | count |
|`column 3` | description | count |

**What I noticed**

> Gaps, duplcates, odd values, name spelling that differ from your other datasets

## 10.

- **Source:**
- **Retrieved:**
- **File:** `data/raw/filename`
- **Format:**
- **Geometry Type:**
- **Feature Count:**
- **CRS as Downloaded:**

## Key Columns

| Column | What it Entails | Nulls |
|---|---|---|
|`column 1` | description | count |
|`column 2` | description | count |
|`column 3` | description | count |

**What I noticed**

> Gaps, duplcates, odd values, name spelling that differ from your other datasets

## 11.

- **Source:**
- **Retrieved:**
- **File:** `data/raw/filename`
- **Format:**
- **Geometry Type:**
- **Feature Count:**
- **CRS as Downloaded:**

## Key Columns

| Column | What it Entails | Nulls |
|---|---|---|
|`column 1` | description | count |
|`column 2` | description | count |
|`column 3` | description | count |

**What I noticed**

> Gaps, duplcates, odd values, name spelling that differ from your other datasets

## Cross-Cutting problems

> **Problem 1:**

**Status:** Week 2 not completed. Reprojections and quality checks in Week 3, see [03-data-preparation.md](data-preparation.md).

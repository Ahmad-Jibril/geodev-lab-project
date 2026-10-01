# Data Preparation

## 1. Coordinate System Decision

Lagos State, the chosen CRS is in meters
and it is projected to UTM Zone 31

| S/N | Dataset | CRS as Downloaded | CRS After | Operation |
|---|---|---|---|---|
|1 | Lagos State LGA Boundary | EPSG:4326 | EPSG:32631 | Reprojection |
|2 | Rainfall Data | EPSG:4326 | EPSG:32631 | Reprojection |
|3 | Soil Composition Grids | ESRI:54009 | EPSG:32631 | Reprojection |
|4 | Motorable Road | EPSG:4326 | EPSG:32631 | Reprojection |
|5 | Public & Institutional Land | EPSG:4326 | EPSG:32631 | Reprojection |
|6 | FABDEM (Bare Earth Elevation) | EPSG:4326 | EPSG:32631 | Reprojection |
|7 | Lagos Drainage Network & Canal | EPSG:4326 | EPSG:32631 | Reprojection |
|8 | Land Use Data | EPSG:4326 | EPSG:32631 | Reprojection |
|9 | Google Open Buildings | EPSG:4326 | EPSG:32631 | Reprojection |
|10 | Protected Ecological Reserves | EPSG:4326 | EPSG:32631 | Reprojection |
|11 | Sentinel-1 Satellite Imagery | EPSG:4326 | EPSG:32631 | Reprojection |

> Reprojecting recalculates every coordinate.
> Assigning a CRS only relabels the data

## 2. Clipping to The Study Area

- **Boundary Used:** 
- **Feature before Clipping:** Covered the whole of Nigeria
- **Feature after Clipping:** Covered just the needed area (Lagos State) and erased the 
unneeded data that covered the remaining unneeded part

## 4. The Five Quality Checks

| S/N | Check | Result | Action Taken |
|---|---|---|---|
|1 | Is the *CRS* What I think it is? | Yes | Reprojected them to the required CRS for the project |
|2 | Are there *nulls* in the fields I need? | Yes | I filled the nulls with *'N/A'* |
|3 | Are there duplicate *features?* | No |  |
|4 | Is the *geometry* valid? | Yes |  |
|5 | Does *coverage* cover the whole study? | Partially (i.e just a little part is left out) for some datasets and Yes for the rest |  |

## 5. Problems Found, and What I did
  
Some layers were taking a while to load because of the file format, so I exported them as GeoPackages instead. For example, I converted the Motorable Roads layer from `.osm.pbf` to `.gpkg`, which made processing much faster.

## 6. The Analysis Ready Output

- **File:** 
- **Format:** GeoTIFF(s) and GeoPackage(s), 
- **CRS:** EPSG:32631
- **Features:** Vector and Rasters
- **Produced:** Manually in QGIS

---

**Status:** Week 3 complete. First spatial analysis in Week 4, see [04-month-1-summary.md](04-month-1-summary.md).
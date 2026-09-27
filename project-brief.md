# My Project Brief

**Week 1 Deliverables.** GeoDev Lab Africa Cohort 1.

**Author:** *Ahmad Jibril-Adeyemi* 

---

## 1. The Question

> Which buildings and roads in **Lagos State** are at high risk of flooding, and
> where are the ***three (3)*** best public sites to build water basins per
> **Local Government Area (LGA)** to help manage that risk?

## 2. Why This Question

> Every year, ***Lagos State floods*** — and it's not just a traffic headache.
> Thousands of ***buildings*** end up being ***flooded, roads*** people rely on to
> get to work/school or move goods ***become impassable,*** and the financial and health
> toll falls hardest on communities that can least afford it.
> Most existing research stops at showing where the danger is — producing
> maps and hazard models — without going the extra step of identifying actual,
> buildable solutions that city authorities could put into action.

> I've experienced this flooding firsthand, and it's what's driving me to
> spend the next twelve months doing the deeper work that will ultimately
> identify ***three (3)*** real public sites for water retention basins
> across each ***Local Government Area (LGA)*** — solutions
> that would directly protect the people and infrastructures at risk.

## 3. Study Area

> ***Lagos State, Nigeria,*** using its official state and Local Government Area (LGA) boundaries as defined by national administrative records.

## 4. What I Mean by The Term

> ``Water basins`` can be *underground concrete tanks, small soakaway pits,
> or roadside drainage channels* that let water soak into the ground.

## 5. Datasets

| S/N | Dataset | Role | Source | File Format | File Size 
|---|---|---|---|---|---|
|1 | Lagos State & LGA Boundaries (20 LGAs) | Defines the boundaries for the study area and breaks the analysis down by LGA, so basin sites can be identified within each one | [Google Earth Engine](https://code.earthengine.google.com/) | `GeoJSON` | 50KB |
|2 | FABDEM v1.2 (Bare Earth Elevation Data) | Shows the actual ground elevation with buildings and trees removed, used to work out slope, how water flows across the land, and how wet different areas tend to get — all needed to model where flooding accumulates | [Awesome GEE Community Catalog](https://gee-community-catalog.org/) | `GeoTIFF` | 17.2MB |
|3 | Lagos Drainage Network & Canals | Used to correct the elevation data so that raised roads don't accidentally look like dams blocking water flow, and to measure how close each area is to an actual drainage channel — a key flood risk factor | [OpenStreetMap](https://overpass-turbo.eu/) | `GeoPackage` | 520KB |
|4 | Google Open Buildings V3 | Maps every permanent building across the state, so we can measure how much built-up area falls inside high risk flood zones | [Google Open Buildings](https://source.coop/) | `PARQUET` | 1.06GB
|5 | Complete Drivable Road Network | Breaks roads into 50 meter sections and checks each one against the flood hazard map, to measure how much road length would actually be underwater and how badly that disrupts the road network | [GeoFabrik Nigeria Extract](https://download.geofabrik.de/) | `OSM PBF` | 676MB
|6 | Dynamic World 10m Land Use Data | Measures how much of the ground is paved or built-over versus natural, which determines how much rainfall runs off instead of soaking in — a key input for predicting runoff | [Google Earth Engine](https://code.earthengine.google.com/) | `GeoTIFF` | 3.3MB
|7 | SoilGrids 250m v2.0 (Clay, Sand, Silt) | Maps soil composition to work out how well the ground can absorb water in different areas — important for deciding where a retention basin would actually work | [ISRIC SoilGrids WCS](https://isric.org/) | `GeoTIFF` | 934KB
|8 | CHIRPS Daily Rainfall Data | Provides historical rainfall records, including the heaviest 24 hour storms on record, used to calculate how much water would run off during a serious storm | [Google Earth Engine](https://code.earthengine.google.com/) | `GeoTIFF` | 3KB
|9 | Public & Institutional Land | Provides the pool of candidate sites — schools, transport depots, open spaces, sports grounds — that get screened down to three viable public locations per LGA | [QuickOSM](https://grid3.org/) | `GeoJSON` | 437KB
|10 | Protected Ecological Reserves | Marks off limits areas — protected conservation zones and mangrove reserves — to make sure no retention basin is placed somewhere it shouldn't be | [World Database on Protected Areas (WDPA)](https://www.protectedplanet.net) | `GeoJSON` | 384KB
|11 | Sentinel-1 Satellite Radar Imagery | Checks the flood zones the model predicts against actual satellite images of past flooding during peak rainy seasons, to confirm the model is accurate | [Google Earth Engine](https://code.earthengine.google.com/) | `GeoTIFF` | 1016MB

## 6. What Done Looks Like

> Describe the finished output in two or three sentences
> A map? A table? or both? reproducible by whom?

## Known Risks

- **Risk 1:** What could go wrong and how you will go about it
- **Risk 2:** What could go wrong and how you will go about it

**Status:** Week 1 completed yet. Data acquisition in Week 2, See [02-data-notes.md](data-notes.md).

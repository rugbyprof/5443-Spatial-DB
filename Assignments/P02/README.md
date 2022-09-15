## Project 2 - World Data 
#### Due: 09-20-2022 (Tuesday @ 3:30 p.m.)


## Overview

We are going to download and create tables to hold lots of data that is available for download. Most of our data will come from [HERE](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html). There are more boundary files [HERE](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html) dealing with districts and counties. The files I want you to get are listed below, and I will place them on the cs server. I'll provide the original links as well just in case.

### Data Files

Specifically we want the following data files. Most are shape files, one is a csv.

- Primary US Roads
  - https://www2.census.gov/geo/tiger/TIGER2019/PRIMARYROADS/tl_2019_us_primaryroads.zip
- US Rail Roads
  - http://www2.census.gov/geo/tiger/TIGER2019/RAILS/tl_2019_us_rails.zip
- States
  - https://www2.census.gov/geo/tiger/TIGER2021/STATE/tl_2021_us_state.zip
- Military Bases 
  - https://www2.census.gov/geo/tiger/TIGER2021/MIL/tl_2021_us_mil.zip
- Airports
  - https://cs.msutexas.edu/~griffin/data/Airport_and_Plane_Data/airports.csv

### Import and Create Tables

I used `shp2pgsql`:

`shp2pgsql -s 4326 -I INPUTSHAPEFILE.shp TABLENAME| psql  -d DATABASENAME -U USERNAME`

### Create and index on the spatial column in your table

- http://postgis.net/workshops/postgis-intro/indexing.html


### FYI

Will talk more about this later.

```sql
select *,geom::json from ch01.airports;

select *,geom::json from primary_roads where fullname like 'I- 10';
```

## Deliverables:

- Create a folder in your github `Assignments` folder called `P02A`
- Export the sql to create your tables and indexes into 1 file per table.
- Select the first 5-10 rows and output those in a manner that's readable, again, 1 per table.
  


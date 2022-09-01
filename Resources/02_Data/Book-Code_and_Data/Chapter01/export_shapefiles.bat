@echo off
for /f "tokens=1-3 delims=, skip=1" %%a in (hs_countries.csv) do (
    echo "Generating shapefile %%b.shp for country %%a (%%b) containing %%c features"
    ogr2ogr out_shapefiles/%%b.shp PG:"dbname='postgis_cookbook' user='me' password='mypassword'" -lco SCHEMA=chp01 -sql "SELECT ST_Transform(hs.the_geom, 4326), hs.acq_date, hs.acq_time, hs.bright_t31 FROM chp01.hotspots as hs JOIN chp01.countries as c ON ST_Contains(c.the_geom, ST_Transform(hs.the_geom, 4326)) WHERE c.iso2 = '%%b'"
)

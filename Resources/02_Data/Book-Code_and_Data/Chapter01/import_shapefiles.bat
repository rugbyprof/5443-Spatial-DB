@echo off
for %%I in (out_shapefiles\*.shp*) do (
    echo Importing shapefile %%~nxI to chp01.hs_uploaded PostGIS table...

ogr2ogr -append -update  -f PostgreSQL PG:"dbname='postgis_cookbook' user='me' password='mypassword'" out_shapefiles/%%~nxI -nln chp01.hs_uploaded -sql "SELECT acq_date, acq_time, bright_t31, '%%~nI' AS iso2, '%date%' AS upload_datetime, 'out_shapefiles/%%~nxI' as shapefile FROM %%~nI"
)
## Placeholder Readme - No Description



ogr2ogr -f "PostgreSQL" PG:"dbname=inAction user=griffin password=1029" ./world -nln ch01.world_borders

ogr2ogr -overwrite -progress -t_srs EPSG:3500 -f "PostgreSQL" PG:"host=localhost port=5432 dbname=inAction user=griffin password=1029" ./world_borders-1-10.json -lco geometry_name=geom 

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/query_speed_1.png" width="300">

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/query_speed_2.png" width="300">

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/query_speed_3.png" width="300">


https://postgis.net/2017/11/07/tip-move-postgis-schema/


https://github.com/jwass/geojsonio.py
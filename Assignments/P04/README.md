## Project 3 - Missile Command (Part 2)
#### Due: 09-29-2022 (Thursday @ 3:30 p.m.)

<center>
<img src="mc.gif" width="300">
</center>

## Overview

I think we may forgo the use of the military installations shape file. If you view the data, you will see most of the bases clustered around the perimeter of the use (aka coastlines). This is a great idea for conventional warfare, but will cause a confusion when visualizing our project. I propose that we use a subset of US cities as our bases. They will be more spread out, and will help with this project. 



| decimals | degrees    | distance |
| :------: | :--------- | -------: |
|    0     | 1.0        |   111 km |
|    1     | 0.1        |  11.1 km |
|    2     | 0.01       |  1.11 km |
|    3     | 0.001      |    111 m |
|    4     | 0.0001     |   11.1 m |
|    5     | 0.00001    |   1.11 m |
|    6     | 0.000001   |  0.111 m |
|    7     | 0.0000001  |  1.11 cm |
|    8     | 0.00000001 |  1.11 mm |

111 m/s = 248.3 mph

```sql
SELECT ST_3DDistance(
			ST_Transform('SRID=4326;POINT(-72.1235 42.3521 1)'::geometry,2163),
			ST_Transform('SRID=4326;POINT(-72.1235 42.3521 20000)'::geometry,2163)
		) As dist_3d
```

```sql
SELECT ST_AsText(ST_Project('POINT(-98 34)'::geography, 555, radians(45.0)));
```


```sql
WITH 
Q1 AS (
    SELECT 'POINT(-98 34)'::geometry as p1
), 

Q2 AS (
     SELECT ST_Project('POINT(-98 34)'::geometry, 555, radians(45.0)) as p2
)

SELECT p1,p2

FROM Q1, Q2;
```


```sql
    WITH 
        Q1 AS (
            SELECT ST_SetSRID(ST_Project('POINT(-98 34)'::geometry, 66600, radians(270))::geometry,4326) as p2
        )
 
SELECT jsonb_build_object(
    'type',       'Feature',
    'geometry',   ST_AsGeoJSON(p2)::jsonb,
	'properties', null
    ) AS json
FROM Q1
```
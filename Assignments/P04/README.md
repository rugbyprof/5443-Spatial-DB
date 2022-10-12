## Project 3 - Missile Command (Part 2)
#### Due: 09-29-2022 (Thursday @ 3:30 p.m.)

<center>
<img src="mc.gif" width="300">
</center>

## Routes

### `getRegion`
As stated in the previous assignment you will be defending a region against incoming missile attacks. The region you will defend will be assigned to you via an api call to `getRegion`. That call will return a geojson object with a list of features that will include:

- Boundary : 1 or more polygons defining your region
- Targets : Points defining the locations in which you are to defend 
- Batteries : Points defining the location of your missile batteries

**make example file**

### `getArsenal`

This route will send back a set of missiles that you have to defend your region. Don't worry about dividing up the missiles up amongst the batteries, we will assume any missile from your arsenal can be fired from any missile battery in your region. Below are a list of missiles and their classifications. 

| Name        | Speed | Blast |
| :---------- | :---: | :---: |
| Atlas       |   1   |   7   |
| Harpoon     |   2   |   8   |
| Hellfire    |   3   |   7   |
| Javelin     |   4   |   7   |
| Minuteman   |   5   |   9   |
| Patriot     |   6   |   6   |
| Peacekeeper |   7   |   6   |
| SeaSparrow  |   8   |   5   |
| Titan       |   8   |   5   |
| Tomahawk    |   9   |   6   |
| Trident     |   9   |   9   |

### Example Response
```json
{
  "Atlas": 20,
  "Harpoon": 13,
  "Hellfire": 12,
  "Javelin": 11,
  "Minuteman": 9,
  "Patriot": 9,
  "Peacekeeper": 8,
  "SeaSparrow": 8,
  "Titan": 5,
  "Tomahawk": 4,
  "Trident": 1,
  "total": 100
}
```

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

### Distance in 3D
```sql
SELECT ST_3DDistance(
			ST_Transform('SRID=4326;POINT(-72.1235 42.3521 1)'::geometry,2163),
			ST_Transform('SRID=4326;POINT(-72.1235 42.3521 20000)'::geometry,2163)
		) As dist_3d
```

### Project New Point
- Given a Point, project a new location given a distance (555) and direction (45)
```sql
SELECT ST_AsText(ST_Project('POINT(-98 34)'::geography, 555, radians(45.0)));
```


### Create New Missile Path
- Using the project point from above
- Give a starting (p1) and ending point (p2) generate a missile path
```sql
WITH 
Q1 AS (
    SELECT 'POINT(-98 34)'::geometry as p1
), 

Q2 AS (
     SELECT ST_Project('POINT(-98 34)'::geometry, 555, radians(45.0))::geometry as p2
)

SELECT ST_MakeLine(ST_Point(ST_X(p1),ST_Y(p1)), ST_Point(ST_X(p2),ST_Y(p2))) as missilePath

FROM Q1, Q2;
```


### Make GeoJson
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


```


select * 
from us_regions as r, us_states AS s
where ST_Within(s.geom,r
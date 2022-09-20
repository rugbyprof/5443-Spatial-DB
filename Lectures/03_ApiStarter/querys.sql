--
CREATE TABLE airports (
    id NUMERIC PRIMARY KEY,
    name text,
    city text,
    country text,
    three_code text,
    four_code text,
    lat DECIMAL(11, 8),
    lon DECIMAL(11, 8),
    elevation text,
    gmt text,
    tz_short text,
    time_zone text,
    type text
);
--
ALTER TABLE ch01.airports
ADD COLUMN geom GEOMETRY(POINT, 4326);
--
UPDATE airports
SET location = ST_SetSRID(ST_MakePoint(lon, lat), 4326);
--
SELECT *,
    ST_Distance(
        'SRID=4326;POINT(-118.41004 33.942791)'::geometry,
        geom
    ) AS dist
FROM airports
ORDER BY dist
LIMIT 10;
--
select count(*)
from ch01.airports a
    join ch01.world_borders b on ST_Intersects(a.geom, b.wkb_geometry)
WHERE b.sov_a3 = 'US1';
--http://postgis.net/workshops/postgis-intro/indexing.html
CREATE INDEX world_borders_idx ON ch01.world_borders USING GIST (wkb_geometry);
--
CREATE INDEX airports_idx ON ch01.airports USING GIST (geom);
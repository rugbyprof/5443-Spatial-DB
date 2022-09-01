-- Importing nonspatial tabular data (CSV) using PostGIS functions
CREATE TABLE chp01.firenews (
  x float8,
  y float8,
  place varchar(100),
  size float8,
  update date,
  startdate date,
  enddate date,
  title varchar(255),
  url varchar(255),
  the_geom geometry(POINT, 4326)
);
-- 
COPY chp01.firenews (
  x,
  y,
  place,
  size,
  update,
  startdate,
  enddate,
  title,
  url
)
FROM '/tmp/firenews.csv' WITH CSV HEADER;
-- 
SELECT COUNT(*)
FROM chp01.firenews;
-- 
SELECT f_table_name,
  f_geometry_column,
  coord_dimension,
  srid,
  type
FROM geometry_columns
where f_table_name = 'firenews';
-- 
UPDATE chp01.firenews
SET the_geom = ST_SetSRID(ST_MakePoint(x, y), 4326);
-- 
UPDATE chp01.firenews
SET the_geom = ST_PointFromText('POINT(' || x || ' ' || y || ')', 4326);
-- 
SELECT place,
  ST_AsText(the_geom) AS wkt_geom
FROM chp01.firenews
ORDER BY place
LIMIT 5;
-- 
CREATE INDEX idx_firenews_geom ON chp01.firenews USING GIST (the_geom);
--
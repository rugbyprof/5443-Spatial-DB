-- verifying PostGIS / PostgreSQL version
SELECT postgis_full_version();
--
SELECT version();
--
CREATE TABLE ch01.lu_franchises (id char(3) PRIMARY KEY, franchise varchar(30));
--
INSERT INTO ch01.lu_franchises(id, franchise)
VALUES ('BKG', 'Burger King'),
  ('CJR', 'Carl''s Jr'),
  ('HDE', 'Hardee'),
  ('INO', 'In-N-Out'),
  ('JIB', 'Jack in the Box'),
  ('KFC', 'Kentucky Fried Chicken'),
  ('MCD', 'McDonald'),
  ('PZH', 'Pizza Hut'),
  ('TCB', 'Taco Bell'),
  ('WDY', 'Wendys');
--
CREATE TABLE ch01.restaurants (
  id serial primary key,
  franchise char(3) NOT NULL,
  geom geometry(point, 2163)
);
--
CREATE INDEX idx_code_restaurants_geom ON ch01.restaurants USING gist(geom);
--
ALTER TABLE ch01.restaurants
ADD CONSTRAINT fk_restaurants_lu_franchises FOREIGN KEY (franchise) REFERENCES ch01.lu_franchises (id) ON UPDATE CASCADE ON DELETE RESTRICT;
--
CREATE INDEX fki_restaurants_franchises ON ch01.restaurants (franchise);
--
CREATE TABLE ch01.highways (
  gid integer NOT NULL,
  feature character varying(80),
  name character varying(120),
  state character varying(2),
  geom geometry(multilinestring, 2163),
  CONSTRAINT pk_highways PRIMARY KEY (gid)
);
--
CREATE INDEX idx_highways ON ch01.highways USING gist(geom);
--#1 create highway
--#3 multilinestring equal area
--#2 add spatial index
--
CREATE TABLE ch01.restaurants_staging (
  franchise text,
  lat double precision,
  lon double precision
);
--
INSERT INTO ch01.restaurants (franchise, geom)
SELECT franchise,
  ST_Transform(
    ST_SetSRID(ST_Point(lon, lat), 4326),
    2163
  ) As geom
FROM ch01.restaurants_staging;
--
CREATE INDEX idx_code_restaurants_geom ON ch01.restaurants USING gist(geom);
--
INSERT INTO ch01.highways (gid, feature, name, state, geom)
SELECT gid,
  feature,
  name,
  state,
  ST_Transform(geom, 2163)
FROM ch01.highways_staging
WHERE feature LIKE 'Principal Highway%';
--
SELECT f.franchise,
  COUNT(DISTINCT r.id) As total
FROM ch01.restaurants As r
  INNER JOIN ch01.lu_franchises As f ON r.franchise = f.id
  INNER JOIN ch01.highways As h ON ST_DWithin(r.geom, h.geom, 1609) - - < co id = "co_code_one_mile_count_2" / >
GROUP BY f.franchise
ORDER BY total DESC;
--
SELECT COUNT(DISTINCT r.id) As total
FROM ch01.restaurants As r
  INNER JOIN ch01.highways As h ON ST_DWithin(r.geom, h.geom, 1609 * 20)
WHERE r.franchise = 'HDE'
  AND h.name = 'US Route 1'
  AND h.state = 'MD';
--
SELECT gid,
  name,
  geom
FROM ch01.highways
WHERE name = 'US Route 1'
  AND state = 'MD';
--
SELECT ST_Union(ST_Buffer(geom, 1609 * 20))
FROM ch01.highways
WHERE name = 'US Route 1'
  AND state = 'MD';
--
SELECT r.geom
FROM ch01.restaurants r
WHERE EXISTS (
    SELECT gid
    FROM ch01.highways
    WHERE ST_DWithin(r.geom, geom, 1609 * 20)
      AND name = 'US Route 1'
      AND state = 'MD'
      AND r.franchise = 'HDE'
  );
--Unused Below
-- loading data server side --
-- Using SQL
COPY ch01.restaurants
FROM '/data/restaurants.csv' DELIMITER ',';
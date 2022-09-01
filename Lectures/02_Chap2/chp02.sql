-- Drop the table in case it exists
DROP TABLE IF EXISTS chp02.xwhyzed CASCADE;
--
-- This table will contain numeric x, y, and z values
CREATE TABLE chp02.xwhyzed (x numeric, y numeric, z numeric) WITH (OIDS = FALSE);
--
-- Not necessary depending on how you created the table
ALTER TABLE chp02.xwhyzed OWNER TO me;
--
-- We will be disciplined and ensure we have a primary key
ALTER TABLE chp02.xwhyzed
ADD COLUMN gid serial;
ALTER TABLE chp02.xwhyzed
ADD PRIMARY KEY (gid);
-- 
-- Add some random data 
INSERT INTO chp02.xwhyzed (x, y, z)
VALUES (random() * 5, random() * 7, random() * 106);
INSERT INTO chp02.xwhyzed (x, y, z)
VALUES (random() * 5, random() * 7, random() * 106);
INSERT INTO chp02.xwhyzed (x, y, z)
VALUES (random() * 5, random() * 7, random() * 106);
INSERT INTO chp02.xwhyzed (x, y, z)
VALUES (random() * 5, random() * 7, random() * 106);
-- Ensure we don't try to duplicate the view
DROP VIEW IF EXISTS chp02.xbecausezed;
--
-- Retain original attributes, but also create a point and y 
CREATE VIEW chp02.xbecausezed AS
SELECT x,
  y,
  z,
  ST_MakePoint(x, y)
FROM chp02.xwhyzed;
-- Create 10 clusters using kmeans and the military base table
-- outputting the cid (cluster id) the gid (base id) and the geometry
-- 10 is the number of clusters you want
-- The ST_Contains is a US bounding box
SELECT ST_ClusterKMeans(geom, 10) OVER() AS cid, gid, geom
FROM military_bases;
WHERE ST_Contains(ST_Polygon('LINESTRING(-129.7844079 19.7433195, -61.9513812 19.7433195, -61.9513812 54.3457868, 
			   -129.7844079 54.3457868, -129.7844079 19.7433195)'::geometry,4326),geom)


-- Create a table using above query
CREATE TABLE base_clusters_kmeans
SELECT ST_ClusterKMeans(geom, 10) OVER() AS cid, gid, geom
FROM military_bases_contus;

-- Create table to store polygons surrounding each cluster
create table base_cluster_polygons as 
SELECT cid,
    ST_ConvexHull(ST_Collect(geom))
    FROM base_clusters_kmeans
    GROUP BY cid;


-- Run DB Scan clustering algorithm on same data as Kmeans
-- eps is basically a distance measure, and minpoints is minimum points to be a cluster
SELECT  ST_ClusterDBSCAN(geom, eps := 3, minpoints := 20)  OVER() AS cid,geom 
    FROM military_bases_contus
	order by cid desc;


-- filter military bases that aren't continental US
SELECT geom FROM military_bases 
WHERE ST_Contains(ST_Polygon('LINESTRING(-129.7844079 19.7433195, -61.9513812 19.7433195, -61.9513812 54.3457868, 
			   -129.7844079 54.3457868, -129.7844079 19.7433195)'::geometry,4326),geom)

--Get bases and the state that they are in:
SELECT
  states.name AS state_name,
  bases.fullname as fullname
FROM states 
JOIN military_bases AS bases
ON ST_Intersects(states.geom, bases.geom)
GROUP BY state_name,fullname
order by state_name

--Distance in meters
SELECT ST_Distance(
	ST_SetSRID(ST_Point(-112.214843 ,54.367758524),4326)::geography,
    ST_SetSRID(ST_Point(-95.449218 ,29.68805274),4326)::geography) as d; 

--Distance in feet
SELECT ST_Distance(
	ST_SetSRID(ST_Point(-112.214843 ,54.367758524),4326)::geography,
    ST_SetSRID(ST_Point(-95.449218 ,29.68805274),4326)::geography)*3.28084 as d; 

--Distance in miles
SELECT ST_Distance(
	ST_SetSRID(ST_Point(-112.214843 ,54.367758524),4326)::geography,
    ST_SetSRID(ST_Point(-95.449218 ,29.68805274),4326)::geography)*3.28084/5280 as d; 
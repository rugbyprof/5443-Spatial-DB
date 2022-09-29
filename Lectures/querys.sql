SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(json.*)::json))
FROM
    (SELECT fullname,
            ST_Centroid(geom)::Geometry(point, 4326) AS geom
     FROM military_bases) as json;


SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(json.*)::json))
FROM
    ( SELECT ST_ClusterKMeans(ST_Centroid(geom),100) OVER() AS cid,
             geom
     FROM military_bases) as json; 


SELECT
  states.name AS state_name,
  bases.fullname as fullname
FROM states 
JOIN military_bases AS bases
ON ST_Intersects(states.geom, bases.geom)
GROUP BY state_name,fullname
order by state_name
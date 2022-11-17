## Project 3 - Missile Command (Pt1)
#### Due: 12-06-2022 (Thursday @ 3:30 p.m.)

<center>
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/mc.gif" width="300">
</center>

1. Provide a function that calculates the area and centroid of the region you must defend.
   - `ST_Area(geom)`

2. Create a bounding box around the area you are assigned. This doesn't mean you need to use it in calculations, but you still need to provide at minimum two points that creates a minimum rectangle around your area.
   - `ST_Envelope(geom)`

3. Using your bounding box, or the polygon of your region, provide 5 missile battery locations that correspond with the centerpoints of the : North, South, East, and West lines bounding your region as well as the centroid of your region for the 5th battery. 
   - There are a few postGis functions to use, however I think these will get the job done. `ST_Envelope` returns a polygon of 5 points where 1st and last are the same. Knowing this we can create the 4 lines that are connected by the 4 points: (p0->p1, p1->2, p2->p3, p3->p4)
     - Then we could do `ST_Centroid` on a "LineString" to get the position for a missile battery on a single line!

4. Provide a function that determines whether or not a projectile will land within your region. Given two radar sweeps, show the landing point and time of a possible strike of a missile. With both radar sweeps, calculating the `drop rate` and `point` of landing, shouldn't be too hard.

5. Those two values (paired with starting and current lon/lat) will allow you to calculate everything necessary to shoot a missile down (as well as where it will land). Your function should be written in PostGres and return a point that includes (lon/lat/time) of when a missile will land.
   
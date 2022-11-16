## Project 3/4 - Missile Command (Pt1)
#### Due: 12-06-2022 (Thursday @ 3:30 p.m.)

<center>
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/mc.gif" width="300">
</center>

1. Provide a function that calculates the area and centroid of the region you must defend.
2. Create a bounding box around the area you are assigned. This doesn't mean you need to use it in calculations, but you still need to provide at minimum two points that creates a minimum rectangle around your area.
3. Using your bounding box, or the polygon of your region, provide 5 missile battery locations that correspond with the centerpoints of the : North, South, East, and West lines bounding your region as well as the centroid of your region for the 5th battery. 
4. Provide a function that determines whether or not a projectile will land within your region. Given two radar sweeps, show the landing point and time of a possible strike of a missile. With both radar sweeps, calculating the `drop rate` and `speed` of an incoming missile is totally possible. Those two values (paired with starting and current lon/lat) will allow you to calculate everything necessary to shoot a missile down (as well as where it will land).
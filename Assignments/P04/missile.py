import math

PI = math.pi

def mph(metersPerSecond):
    return 2.237 * metersPerSecond


def calcPosition(lon,lat,speed,angle,time=1,geojson=False):
    """
        lon (float) : x coordinate
        lat (float) : y coordinate 
        speed (int) : meters per second
        angle (float) : direction in degrees (0-360)
        multiline(bool) : return the next position as point or interpolated line
    """
    if not geojson:
        select = "st_x(p2) as x,st_y(p2) as y"
    else:
        select = "ST_AsGeoJSON(p2)"

    sql = f"""
    WITH 
        Q1 AS (
            SELECT ST_SetSRID(ST_Project('POINT({lon} {lat})'::geometry, {speed*time}, radians({angle}))::geometry,4326) as p2
        )
 
    SELECT {select}
    FROM Q1
    """

    print(sql)
    
class Missile:
    def __init__(self):
        self.speed = 555  # speed in m/s 
        self.blastRadius = 500  # radius in meters
        self.lon = -98.0  # x coord
        self.lat = 34.0  # y coord
        self.alt = 0.0  # z coord (altitude)

    def move(self, dx, dy, dz):
        self.lon += dx
        self.lat += dy
        self.alt += dz
    

calcPosition(-98,34,1110,270,60,True)
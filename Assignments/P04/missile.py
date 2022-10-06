import math
import json
import random 

PI = math.pi


def mph(metersPerSecond):
    return 2.237 * metersPerSecond


def getRandomPointOnBBox(d=None,buffer=0):
    bbox = {
        'l': -124.7844079, # left
        'r': -66.9513812, # right
        't': 49.3457868, # top
        'b': 24.7433195 # bottom
    }

    directions = ['N','S','E','W']

    if not d:
        d = random.shuffle(directions)

    x1 = ((abs(bbox['l']) - abs(bbox['r'])) * random.random() + abs(bbox['r'])) * -1
    x2 = ((abs(bbox['l']) - abs(bbox['r'])) * random.random() + abs(bbox['r'])) * -1
    y1 = (abs(bbox['t']) - abs(bbox['b'])) * random.random() + abs(bbox['b'])
    y2 = (abs(bbox['t']) - abs(bbox['b'])) * random.random()+ abs(bbox['b'])

    if d == 'N':
        start = [x1,bbox['b'] - buffer]
        end = [x2,bbox['t'] + buffer]
    elif d == 'S':
        start = [x1,bbox['t'] + buffer]
        end = [x2,bbox['b'] - buffer]
    elif d == 'E':
        start = [bbox['l']- buffer,y1]
        end = [bbox['r'] + buffer,y2]
    else:
        start = [bbox['r'] + buffer,y1]
        end = [bbox['l'] - buffer,y2]

    return [start,end]



def calcPosition(lon, lat, speed, angle, time=1, geojson=False):
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


if __name__ == '__main__':
    calcPosition(-98, 34, 1110, 270, 60, True)
    print(getRandomPointOnBBox('N',10))
    print(getRandomPointOnBBox('E',7))
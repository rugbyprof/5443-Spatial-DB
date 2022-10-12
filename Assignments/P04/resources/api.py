from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import psycopg2
import json
import random
from math import radians, degrees, cos, sin, asin, sqrt, pow, atan2

"""
           _____ _____   _____ _   _ ______ ____
     /\   |  __ \_   _| |_   _| \ | |  ____/ __ \
    /  \  | |__) || |     | | |  \| | |__ | |  | |
   / /\ \ |  ___/ | |     | | | . ` |  __|| |  | |
  / ____ \| |    _| |_   _| |_| |\  | |   | |__| |
 /_/    \_\_|   |_____| |_____|_| \_|_|    \____/

The `description` is the information that gets displayed when the api is accessed from a browser and loads the base route.
Also the instance of `app` below description has info that gets displayed as well when the base route is accessed.
"""

# description = """🚀
# ## 🚀Missile Command🚀
# ### But Not Really
# """


# This is the `app` instance which passes in a series of keyword arguments
# configuring this instance of the api. The URL's are obviously fake.
app = FastAPI(
    title="🚀Missile Command🚀",
    version="0.0.1",
    terms_of_service="🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

"""
  ___   _ _____ _
 |   \ /_\_   _/_\
 | |) / _ \| |/ _ \
 |___/_/ \_\_/_/ \_\
"""

# stores defenders playing missile command
participants = {}

missile_data = {
    "missiles": {
        "Atlas": {"speed": 1, "blast": 7},
        "Harpoon": {"speed": 2, "blast": 8},
        "Hellfire": {"speed": 3, "blast": 7},
        "Javelin": {"speed": 4, "blast": 7},
        "Minuteman": {"speed": 5, "blast": 9},
        "Patriot": {"speed": 6, "blast": 6},
        "Peacekeeper": {"speed": 7, "blast": 6},
        "SeaSparrow": {"speed": 8, "blast": 5},
        "Titan": {"speed": 8, "blast": 5},
        "Tomahawk": {"speed": 9, "blast": 6},
        "Trident": {"speed": 9, "blast": 9},
    },
    "speed": {
        1: {"ms": 111, "mph": 248.307},
        2: {"ms": 222, "mph": 496.614},
        3: {"ms": 333, "mph": 744.921},
        4: {"ms": 444, "mph": 993.228},
        5: {"ms": 555, "mph": 1241.535},
        6: {"ms": 666, "mph": 1489.842},
        7: {"ms": 777, "mph": 1738.149},
        8: {"ms": 888, "mph": 1986.456},
        9: {"ms": 999, "mph": 2234.763},
    },
    "blast": {1: 200, 2: 300, 3: 400, 4: 500, 5: 600, 6: 700, 7: 800, 8: 900, 9: 1000},
}


"""
  _      ____   _____          _         _____ _                _____ _____ ______  _____
 | |    / __ \ / ____|   /\   | |       / ____| |        /\    / ____/ ____|  ____|/ ____|
 | |   | |  | | |       /  \  | |      | |    | |       /  \  | (___| (___ | |__  | (___
 | |   | |  | | |      / /\ \ | |      | |    | |      / /\ \  \___ \\___ \|  __|  \___ \
 | |___| |__| | |____ / ____ \| |____  | |____| |____ / ____ \ ____) |___) | |____ ____) |
 |______\____/ \_____/_/    \_\______|  \_____|______/_/    \_\_____/_____/|______|_____/
"""

# def dropRate(speed, distance, altitude):
#     time = distance / speed
#     return {"time": time, "rate": altitude / time}


def dsba(pos1, pos2):
    """
    Params:
        pos1 (Position) : lon,lat,altitude,time
        pos2 (Position) : lon,lat,altitude,time
    Returns:
        distance: in meters
        speed: in meters per second
        bearing: degrees where 90=east and 270=west
        dropRate: where I calculate the drop rate of the missile
    """

    bearing = compass_bearing(pos1, pos2)
    distance = haversineDistance(pos1.lon,pos1.lat,pos2.lon,pos2.lat,"meters")
    timeDiff = abs(pos1.time-pos2.time)
    altDiff = pos1.altitude-pos2.altitude
    speed = distance * timeDiff
    dropRate = altDiff / timeDiff

    d = round(distance,2)
    s = round(speed,2)
    b = round(bearing,2)
    a = round(dropRate,2)
    return {"distance":d,"speed":s,"bearing":b,"dropRate":a}


def haversineDistance(lon1, lat1, lon2, lat2, units="meters"):
    """Calculate the great circle distance in kilometers between two points on the earth (start and end) where each point
        is specified in decimal degrees.
    Params:
        lon1  (float)  : decimel degrees longitude of start (x value)
        lat1  (float)  : decimel degrees latitude of start (y value)
        lon2  (float)  : decimel degrees longitude of end (x value)
        lat3  (float)  : decimel degrees latitude of end (y value)
        units (string) : miles or km depending on what you want the answer to be in
    Returns:
        distance (float) : distance in whichever units chosen
    """
    radius = {"km": 6371, "miles": 3956,"meters": 6371000,"feet":20887680}

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = radius[units]  # choose miles or km for results

    return c * r


def compass_bearing(PositionA, PositionB):
    """Calculates the bearing between two points.
        The formulae used is the following:
            θ = atan2(sin(Δlong).cos(lat2),cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
    Source:
        https://gist.github.com/jeromer/2005586
    Params:
        pointA  : The tuple representing the latitude/longitude for the first point. Latitude and longitude must be in decimal degrees
        pointB  : The tuple representing the latitude/longitude for the second point. Latitude and longitude must be in decimal degrees
    Returns:
        (float) : The bearing in degrees
    """

    if not isinstance(PositionA, Position) or not isinstance(PositionB, Position):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = radians(PositionA.lat)
    lat2 = radians(PositionB.lat)

    diffLong = radians(PositionB.lon - PositionA.lon)

    x = sin(diffLong) * cos(lat2)
    y = cos(lat1) * sin(lat2) - (sin(lat1) * cos(lat2) * cos(diffLong))

    initial_bearing = atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


class Position(object):
    def __init__(self, **kwargs):
        self.lon = kwargs.get("lon", 0.0)
        self.lat = kwargs.get("lat", 0.0)
        self.altitude = kwargs.get("altitude", 0.0)
        self.time = kwargs.get("time", 0.0)

    def __str__(self):
        lon = round(self.lon,4)
        lat = round(self.lon,4)
        alt = round(self.lon,4)
        time = round(self.lon,4)
        return f"{lon}, {lat}, {alt}, {time}"



class MissileInfo(object):
    @staticmethod
    def missile(name):
        if not name in list(missile_data["missiles"].keys()):
            return {"error": "Missile doesn't exist."}
        data = missile_data["missiles"][name]
        speed = missile_data["speed"][data["speed"]]
        blast = missile_data["blast"][data["blast"]]
        return {"speed": speed, "blast": blast}

    @staticmethod
    def blast(id):
        return missile_data["speeds"][id]

    @staticmethod
    def speed(id):
        return missile_data["blasts"][id]


class MissileServer(object):
    def __init__(self):
        pass

    def registerDefender(self, id):
        participants["defender"][id] = {}


class DatabaseCursor(object):
    """https://stackoverflow.com/questions/32812463/setting-schema-for-all-queries-of-a-connection-in-psycopg2-getting-race-conditi
    https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
    """

    def __init__(self, conn_config_file):
        with open(conn_config_file) as config_file:
            self.conn_config = json.load(config_file)

    def __enter__(self):
        self.conn = psycopg2.connect(
            "dbname='"
            + self.conn_config["dbname"]
            + "' "
            + "user='"
            + self.conn_config["user"]
            + "' "
            + "host='"
            + self.conn_config["host"]
            + "' "
            + "password='"
            + self.conn_config["password"]
            + "' "
            + "port="
            + self.conn_config["port"]
            + " "
        )
        self.cur = self.conn.cursor()
        self.cur.execute("SET search_path TO " + self.conn_config["schema"])

        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # some logic to commit/rollback
        self.conn.commit()
        self.conn.close()


class DBQuery(object):
    def __init__(self, config):
        self.result = {}
        self.config = config
        self.limit = 1000
        self.offset = 0

    def __query(self, sql, qtype=3):
        with DatabaseCursor(self.config) as cur:
            print(sql)
            cur.execute(sql)

            if qtype == 1:
                self.result["data"] = cur.fetchone()
            elif qtype == 2:
                self.result["data"] = cur.fetchmany()
            else:
                self.result["data"] = cur.fetchall()

            self.result["limit"] = self.limit
            self.result["offset"] = self.offset
            self.result["sql"] = sql
            self.result["success"] = cur.rowcount > 0
            self.result["effectedRows"] = cur.rowcount
        return self.result

    def queryOne(self, sql, **kwargs):

        limit = kwargs.get("limit", self.limit)
        offset = kwargs.get("offset", self.offset)
        self.result["offset"] = offset

        if limit:
            self.limit = limit

        return self.__query(sql + f" LIMIT {self.limit} OFFSET {offset}")

    def queryAll(self, sql, **kwargs):

        limit = kwargs.get("limit", self.limit)
        offset = kwargs.get("offset", self.offset)
        self.result["offset"] = offset

        if limit:
            self.limit = limit

        return self.__query(sql + f" LIMIT {self.limit} OFFSET {offset}")

    def queryMany(self, sql, **kwargs):

        limit = kwargs.get("limit", self.limit)
        offset = kwargs.get("offset", self.offset)
        self.result["offset"] = offset

        if limit:
            self.limit = limit
        return self.__query(sql + f" LIMIT {self.limit} OFFSET {offset}")


conn = DBQuery(".config.json")



def nextLocation(lon: float, lat: float, speed: float, bearing: float, time:int=1, geojson: int=0):
    """
    lon (float) : x coordinate
    lat (float) : y coordinate
    speed (int) : meters per second
    bearing (float) : direction in degrees (0-360)
    geojson(bool) : return the next position as a geojson object
    """
    if not geojson:
        select = "st_x(p2) as x,st_y(p2) as y"
    else:
        select = "ST_AsGeoJSON(p2)"

    sql = f"""
    WITH 
        Q1 AS (
            SELECT ST_SetSRID(ST_Project('POINT({lon} {lat})'::geometry, {speed*time}, radians({bearing}))::geometry,4326) as p2
        )
 
    SELECT {select}
    FROM Q1
    """

    return conn.queryOne(sql)


"""
  _____   ____  _    _ _______ ______  _____
 |  __ \ / __ \| |  | |__   __|  ____|/ ____|
 | |__) | |  | | |  | |  | |  | |__  | (___
 |  _  /| |  | | |  | |  | |  |  __|  \___ \
 | | \ \| |__| | |__| |  | |  | |____ ____) |
 |_|  \_\\____/ \____/   |_|  |______|_____/

 This is where your routes will be defined. Remember they are really just python functions
 that will talk to whatever class you write above. Fast Api simply takes your python results
 and packagres them so they can be sent back to your programs request.
"""


@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")


@app.get("/missile_path")
def missilePath(d: str = None, buffer: float = 0):
    bbox = {
        "l": -124.7844079,  # left
        "r": -66.9513812,  # right
        "t": 49.3457868,  # top
        "b": 24.7433195,  # bottom
    }

    directions = ["N", "S", "E", "W"]

    if not d:
        d = random.shuffle(directions)

    x1 = ((abs(bbox["l"]) - abs(bbox["r"])) * random.random() + abs(bbox["r"])) * -1
    x2 = ((abs(bbox["l"]) - abs(bbox["r"])) * random.random() + abs(bbox["r"])) * -1
    y1 = (abs(bbox["t"]) - abs(bbox["b"])) * random.random() + abs(bbox["b"])
    y2 = (abs(bbox["t"]) - abs(bbox["b"])) * random.random() + abs(bbox["b"])

    if d == "N":
        start = [x1, bbox["b"] - buffer]
        end = [x2, bbox["t"] + buffer]
    elif d == "S":
        start = [x1, bbox["t"] + buffer]
        end = [x2, bbox["b"] - buffer]
    elif d == "E":
        start = [bbox["l"] - buffer, y1]
        end = [bbox["r"] + buffer, y2]
    else:
        start = [bbox["r"] + buffer, y1]
        end = [bbox["l"] - buffer, y2]

    return [start, end]


@app.get("/getArsenal")
def getArsenal(id: str = None, total: int = 50):
    """ Returns a missile arsenal randomly generated weighted to 
        give more slower weaker missiles that fast and strong.
    Params:
        id (str) : id of the team 
        total (int) : total number of missiles to be issued
    """
    names = list(missile_data["missiles"].keys())

    missiles = []


    i = len(names)*2
    for name in sorted(names):
        print(name,i)
        missiles.extend([name] * i)
        print(len(missiles))
        i -= 2

    random.shuffle(missiles)

    missileCount = {}

    sum = 0
    for name in names:
        missileCount[name] = missiles[:total].count(name)
        
        if missileCount[name] == 0:
            missileCount[name] += 1
            missileCount["Atlas"] -= 1

        sum += missileCount[name] 
        
    missileCount['total'] = sum
    return missileCount


@app.get("/radar_sweep")
def radar_sweep():
    pass

@app.get("/region")
def region(numRegions : int = 6,id : int = -1):
    if id < 0:
        where = " "
    else:
        where = f" WHERE cid = {id}"

    sql = f"SELECT cid,geom::json FROM public.regions_{numRegions} {where}"
    print(sql)
    res = conn.queryOne(sql)

    print(res['data'][:2])

    # with open('zzz2.json','w') as f:
    #     json.dumps(res['data'],indent=4)

    fc = {
        "type": "FeatureCollection",
        "features": []
    }
    feature = {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": None
      }
    }

    return fc

  


@app.get("/missileInfo")
def missileInfo(name: str):
    return MissileInfo.missile(name)


"""
This main block gets run when you invoke this file. How do you invoke this file?

        python api.py 

After it is running, copy paste this into a browser: http://127.0.0.1:8080 

You should see your api's base route!

Note:
    Notice the first param below: api:app 
    The left side (api) is the name of this file (api.py without the extension)
    The right side (app) is the bearingiable name of the FastApi instance declared at the top of the file.
"""
if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8080, log_level="debug", reload=True)
    print(MissileInfo.missile("Patriot"))

    A = Position(lon=-94, lat=35, altitude=13000, time=0)
    B = Position(lon=-112.5, lat=35, altitude=13000, time=1)
    C = Position(lon=-112, lat=35.5, altitude=12980, time=4)
    print(compass_bearing(B, C))
    print(dsba(C, B))

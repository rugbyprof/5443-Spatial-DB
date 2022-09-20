from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

import psycopg2
import json
import csv


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

title = """🚀
# Api Starter
"""

description = """This is a basic api using the `fastApi` library. """

app = FastAPI(
    title=title,
    description=description,
    version="0.0.1",
    terms_of_service="http://yourdomain.us/terms/",
    contact={
        "name": "Administrator",
        "url": "http://yourdomain.us/worldle/contact/",
        "email": "chacha@yourdomain.us",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")


@app.get("/countryNames")
async def countryNames():
    sql = """
        SELECT name FROM ch01.world_borders
        ORDER BY name"""
    return conn.queryAll(sql)


@app.get("/airports")
async def airports(
    limit: int = 1000, offset: int = 0, geojson: str = False, country: str = None
):
    if country:
        where = f" WHERE country like '{country}'"
    else:
        where = ""

    if not geojson:
        sql = "SELECT * FROM ch01.airports " + where
    else:
        sql = "SELECT ST_AsGeoJSON(t.*) FROM ch01.airports AS t" + where
    result = conn.queryMany(sql, limit=limit, offset=offset)
    if geojson:
        for i in range(len(result["data"])):
            result["data"][i] = json.loads(result["data"][i][0])
        result = {"type": "FeatureCollection", "features": result["data"]}
        with open("map.geojson", "w") as wf:
            json.dump(result, wf)

    return result


@app.get("/airportsCountry")
async def airportsInCountry(name: str = None, count: bool = False):
    sql = "SELECT "
    if count:
        sql += "COUNT(a.*) "
    else:
        sql += "a.* "

    sql += f"""
            FROM ch01.airports a
            JOIN ch01.world_borders b ON ST_Intersects(a.geom, b.wkb_geometry)
            WHERE b.name like '{name}'"""
    return conn.queryMany(sql)


# SELECT b.name,count(a.*) as count
# FROM ch01.airports a
#     JOIN ch01.world_borders b ON ST_Intersects(a.geom, b.wkb_geometry)
# group by b.name order by count desc


@app.get("/closestAirport")
async def closestAirport(lon: float, lat: float, limit: int = 10):
    sql = f"""SELECT *,
                ST_Distance(
                    'SRID=4326;POINT({lon} {lat})'::geometry,geom) AS dist
            FROM ch01.airports
            ORDER BY dist
    """
    print(sql)
    return conn.queryMany(sql, limit=limit)


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8080, log_level="debug", reload=True)

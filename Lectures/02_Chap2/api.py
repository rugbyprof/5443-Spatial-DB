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


description = """🚀
## Api what
### With Better Distance Calculations
"""

app = FastAPI(
    title="Api what",
    description=description,
    version="0.0.1",
    terms_of_service="http://killzonmbieswith.us/worldleterms/",
    contact={
        "name": "Worldle Clone",
        "url": "http://killzonmbieswith.us/worldle/contact/",
        "email": "chacha@killzonmbieswith.us",
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


@app.get("/restaurants")
async def restaurants():
    sql = "select * from ch01.restaurant"

    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchall()


@app.get("/restaurant/{franchise}")
async def restaurants(franchise):
    sql = f"""SELECT * from ch01.restaurants 
              WHERE franchise = '{franchise}'"""

    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchall()


@app.get("/restaurantCount")
async def restaurants(franchise: str):
    sql = f"""SELECT count(*) from ch01.restaurants 
              WHERE franchise = '{franchise}'"""

    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchone()


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8080, log_level="debug", reload=True)

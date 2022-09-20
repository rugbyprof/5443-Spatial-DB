# pip install psycopg2

import psycopg2
import json
import csv


def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def is_float(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


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


create_extension = """CREATE EXTENSION postgis;"""

# create_extension = """DROP EXTENSION postgis CASCADE;
# SET search_path to ch01;
# CREATE EXTENSION postgis;"""


alter_db = """ALTER DATABASE cookbook SET search_path=chp02,public;
"""

drop_table = "DROP TABLE  IF EXISTS ch01.airports;"


create_table = """CREATE TABLE airports (
    id NUMERIC PRIMARY KEY,
    name VARCHAR(64) NOT NULL,

    city VARCHAR(32) NOT NULL,
    country VARCHAR(256) NOT NULL,
    three_code VARCHAR(3) NOT NULL,
    four_code VARCHAR(4) NOT NULL,
    lat DECIMAL(11,8) NOT NULL,
    lon DECIMAL(11,8)  NOT NULL,
    elevation VARCHAR(10),
    gmt VARCHAR(10),
    tz_short VARCHAR(2),
    time_zone VARCHAR(32),
    type VARCHAR(32),
    location GEOMETRY(POINT, 4326));"""

load_table = """COPY airports (
        id,name,city,country,three_code,four_code,
        lat,lon,elevation,gmt,tz_short,time_zone,
        type
    ) FROM 'airports.csv';
"""


update_location = """UPDATE airports
SET location = ST_SetSRID(ST_MakePoint(lon,lat), 4326);"""

"""
-- select ST_AsEWKT(location,1) from airports
-- WHERE id = 677;



SELECT *, ST_Distance('SRID=4326;POINT(-118.41004 33.942791)'::geometry, location) AS dist
FROM airports
ORDER BY dist LIMIT 10;
"""

if __name__ == "__main__":
    with DatabaseCursor(".config.json") as cur:
        # cur.execute(create_extension)
        cur.execute(drop_table)
        cur.execute(create_table)

    with DatabaseCursor(".config.json") as cur:
        with open("airports2.csv", newline="") as csvfile:
            data = csv.reader(csvfile, delimiter=",")
            for row in data:

                newRow = []
                for col in row:
                    if "\\" in col:
                        col = "0"
                    if "'" in col:
                        col = col.replace("'", "`")
                    if not is_float(col) and not is_integer(col):
                        col = "'" + col + "'"
                    elif col.lower() == "nan":
                        col = "'" + col + "'"
                    newRow.append(col)
                row = ", ".join(newRow)
                sql = f"INSERT INTO ch01.airports VALUES ({row});"
                # print(sql)

                cur.execute(sql)

        # sql = "select * from airports;"

        # cur.execute(sql)

        # print(cur.fetchall())

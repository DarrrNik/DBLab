import pandas
import sqlalchemy
from time import perf_counter
import duckdb
import sqlite3
from sqlalchemy import create_engine
import psycopg2

#host name in pgadmin
host = ""
#user name in pgadmin
user = ""
#user password in pgadmin
password = ""
#database name in pgadmin
database = ""
#port number in pgadmin
port = ""
#table name in pgadmin
tableName = ""

#path to .db file
dbPath = ""

#path to big csv file
bigCsvPath = ""

#path to tiny csv file
tinyCsvPath = ""

t_DuckDB = True 
t_Pandas = True
t_psycopg2 = True
t_SQLAlchemy = True
t_SQLite = True

#server in pgadmin
server = f"postgresql://{user}:{password}@{host}:{port}/{database}"

queries = [ 

    f"""SELECT "VendorID", COUNT(*)
    FROM "{tableName}" GROUP BY 1;""",

    f"""SELECT "passenger_count", AVG("total_amount")
    FROM "{tableName}" GROUP BY 1;""",

    f"""SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*)
    FROM "{tableName}" GROUP BY 1, 2;""",

    f"""SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
    FROM "{tableName}" GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",

]

sqlQueries = [
    f"""SELECT "VendorID", COUNT(*)
    FROM "{tableName}" GROUP BY 1;""",

    f"""SELECT "passenger_count", AVG("total_amount")
    FROM "{tableName}" GROUP BY 1;""",

    f"""SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), COUNT(*)
    FROM "{tableName}" GROUP BY 1, 2;""",

    f"""SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
    FROM "{tableName}" GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",

]


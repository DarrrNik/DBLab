from config import *
import funcs

import TryPostgres
import TrySQLite
import TrySQLAlchemy
import TryPandas
import TryDuckDB

funcs.create_db_from_csv()

if t_SQLite: print("SQLite:", TrySQLite.try_sqlite3())
if t_DuckDB: print("DuckDB:", TryDuckDB.try_duckdb())
if t_psycopg2: print("Postgres:", TryPostgres.try_psycopg2())
if t_SQLAlchemy: print("SQLAlchemy:", TrySQLAlchemy.try_sqlalchemy())
if t_Pandas: print("Pandas:", TryPandas.try_pandas())
from config import *
import funcs

import TryPostgres
import TrySQLite
import TrySQLAlchemy
import TryPandas
import TryDuckDB

funcs.create_db_from_csv()

print("SQLite:", TrySQLite.try_sqlite3())
print("DuckDB:", TryDuckDB.try_duckdb())
print("Postgres:", TryPostgres.try_psycopg2())
print("SQLAlchemy:", TrySQLAlchemy.try_sqlalchemy())
print("Pandas:", TryPandas.try_pandas())
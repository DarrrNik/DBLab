from config import *
import os

def create_db_from_csv():    
    engine = create_engine(server)

    if database not in sqlalchemy.inspect(engine).get_table_names(): 
        print("Creating postgres database")       
        csvData = pandas.read_csv(tinyCsvPath)

        csvData["tpep_pickup_datetime"] = pandas.to_datetime(csvData["tpep_pickup_datetime"])
        csvData["tpep_dropoff_datetime"] = pandas.to_datetime(csvData["tpep_dropoff_datetime"])

        csvData.to_sql(database, engine, if_exists="replace", index=False, chunksize = 1000)
    else:
        print("Postgres database is already created")
    engine.dispose()

    if not os.path.isfile(dbPath):
        print("Creating .db file")
        conn = sqlite3.connect(dbPath)
        csvData = pandas.read_csv(bigCsvPath)

        csvData["tpep_pickup_datetime"] = pandas.to_datetime(csvData["tpep_pickup_datetime"])
        csvData["tpep_dropoff_datetime"] = pandas.to_datetime(csvData["tpep_dropoff_datetime"])

        csvData.to_sql(database, conn, if_exists='replace', index=False)

        conn.close()
    else:
        print(".db file is already created")
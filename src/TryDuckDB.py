from config import *

def try_duckdb():
    countTimes = []
    try:
        duckdb.install_extension("sqlite")
        conn = duckdb.connect(dbPath)
        cursor = conn.cursor()
        for j in range(len(queries)):
            trytime = 0
            for i in range(20):
                start = perf_counter()
                cursor.execute(queries[j])
                finish = perf_counter()
                trytime += finish - start
            countTimes.append(trytime / 20)
    except Exception as er:
        print("Everything is bad, nothing works in \"try_duckdb\".", er)
    finally:
        cursor.close()
        conn.close()
        return countTimes
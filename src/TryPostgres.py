from config import *

def try_psycopg2():
    countTimes = []
    try:
        conn = psycopg2.connect(
            host = host, 
            user = user, 
            password = password, 
            database = database
            )

        cursor = conn.cursor()

        for i in range(len(queries)):
            tryTime = 0
            for j in range(20):
                start = perf_counter()
                cursor.execute(queries[i])
                finish = perf_counter()
                tryTime += finish - start
            countTimes.append(tryTime / 20)
    except psycopg2.Error as er:
        print("Everything is bad, nothing works in \"try_psycopg2\".", er)
    finally:
        cursor.close()
        conn.close()
        return countTimes
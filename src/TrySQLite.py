from config import *

def try_sqlite3():
    countTimes = []
    try:
        conn = sqlite3.connect(dbPath)
        cursor = conn.cursor()

        for i in range(len(sqlQueries)):
            tryTime = 0
            for j in range(20):
                start = perf_counter()
                cursor.execute(sqlQueries[i])
                finish = perf_counter()
                tryTime += finish - start
            countTimes.append(tryTime / 20)
    except sqlite3.Error as er:
        print("Everything is bad, nothing works in \"try_sqlite3\".", er)
    finally:
        cursor.close()
        conn.close()
        return countTimes


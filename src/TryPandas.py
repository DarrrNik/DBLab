from config import *

def try_pandas():
    countTimes = []
    try:
        engine = create_engine(server)
        for i in range(len(queries)):
            tryTime = 0
            for j in range(20):
                start = perf_counter()
                pandas.read_sql(queries[i], con = engine)
                finish = perf_counter()
                tryTime += finish - start
            countTimes.append(tryTime / 20)
    except Exception as er:
        print("Everything is bad, nothing works in \"try_pandas\".", er)
    finally:
        engine.dispose()
        return countTimes
    
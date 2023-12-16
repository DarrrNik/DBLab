from config import *

def try_sqlalchemy():    
    countTimes = []
    try:
        engine = sqlalchemy.create_engine(server, echo = False)
        conn = engine.connect()
        for j in range(len(queries)):
            trytime = 0
            for i in range(20):
                start = perf_counter()
                conn.execute(sqlalchemy.text(queries[j]))
                finish = perf_counter()
                trytime += finish - start
            countTimes.append(trytime / 20)
    except Exception as er:
        print("Everything is bad, nothing works in \"try_sqlalchemy\".", er)
    finally:
        conn.close()
        return countTimes


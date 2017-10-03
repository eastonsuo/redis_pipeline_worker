# input task into worker
import random
import time
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def do_something(arg1,arg2):
    logger.info("Performing logging with arg1=%s and arg2=%s"%(arg1,arg2))
    time.sleep(random.uniform(0.0,1))


def init_redis():
    import redis
    global r
    r = redis.Redis(
        host='localhost',
        port=6379
    )


def add_tasks():
    import dill
    NUM_TASKS = 100
    logger.info("Generating %s tasks" % NUM_TASKS)
    for i in range(NUM_TASKS):
        a1 = random.uniform(0,100)
        a2 = random.uniform(0,100)
        data = dill.dumps((do_something,[a1,a2],logger))
        r.lpush("tasks", data)

if __name__ == "__main__":
    init_redis()
    add_tasks()
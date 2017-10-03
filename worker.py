import redis
import dill
import time
import logging
import random

if __name__ == '__main__':
    r = redis.Redis(host='localhost',port=6379)
    while True:
        if r.exists('tasks'):
            key, data = r.brpop('tasks')
            d_func, d_args ,logger = dill.loads(data)
            d_func(*d_args)

import redis
from src.fact import Fact
import random


class RedisInterface:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host, port, db)

    def save(self, key, content):
        self.r.set(key, content)

    def random_fact(self):
        facts = self.r.keys('*')
        if not facts:
            return {"error": "no fact available"}

        key = random.choice(facts)
        fact = Fact(self.r.get(key).decode('utf-8'))
        return {"fact": fact.info, "year": fact.year}

    def flush_db(self):
        self.r.flushdb()

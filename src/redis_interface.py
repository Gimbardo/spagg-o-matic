import redis
from src.fact import Fact
import random

class RedisInterface:
  def __init__(self, host='localhost', port=6379, db=0):
    self.r = redis.Redis(host, port, db)

  def save(self, key, content):
    self.r.set(key, content)

  def random_fact(self):
    key = random.choice(self.r.keys('*'))
    fact = Fact(self.r.get(key).decode('utf-8'))
    return {fact.year: fact.info}

  def flush_db(self):
    self.r.flushdb()

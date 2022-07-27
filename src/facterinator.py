import redis

class Facterinator:
  def __init__(self):
    r = redis.Redis(host='localhost', port=6379, db=0)

  def save_fact(self, fact):
    r.set(year, fact)

  def random_fact(self):
    return {"year": "here's a fact"}
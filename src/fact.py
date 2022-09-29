
class Fact:
  def __init__(self, content):
    content = content.replace("–","-")
    self.year = content.split("-")[0].strip()
    self.info = '-'.join(content.split("-")[1:])[1:]

  def save(self, redis_interface, key):
    redis_interface.save(key, self.year+" - "+self.info)
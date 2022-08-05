import datetime
from requests import get
import wikipediaapi
from src.redis_interface import RedisInterface
from src.fact import Fact

key = 0

redisInterface = RedisInterface()

today = datetime.date.today()
month = today.strftime("%B")
day = today.strftime("%d")

wikipedia = wikipediaapi.Wikipedia('en')
wiki_page = wikipedia.page(f'{month}_{day}')

redisInterface.flush_db()

for section in wiki_page.sections:
  if(section.title == "Events"):
    for sub_section in section.sections[1:]:
      for event in sub_section.text.split("\n"):
        Fact(event).save(redisInterface, key)
        key += 1
#!/usr/bin/env python

import datetime
from requests import get
import wikipediaapi
from src.redis_interface import RedisInterface
from src.fact import Fact
import logging
import os

class Syncher:
  def __init__(self):
    self.redisInterface = RedisInterface(host= os.getenv('REDIS_ADDRESS'))

  def synch(self):
    logging.info("Synching daily facts")
    key = 0
    today = datetime.date.today()
    month = today.strftime("%B")
    day = today.strftime("%d")

    wikipedia = wikipediaapi.Wikipedia('en')
    wiki_page = wikipedia.page(f'{month}_{day}')

    self.redisInterface.flush_db()

    for section in wiki_page.sections:
      if(section.title == "Events"):
        for sub_section in section.sections[1:]:
          for event in sub_section.text.split("\n"):
            Fact(event).save(self.redisInterface, key)
            key += 1
import datetime
from requests import get
import wikipediaapi

def print_events(events, level=0):
    for event in events.sections:
      print(f"{event.text}")

today = datetime.date.today()
month = today.strftime("%B")
day = today.strftime("%d")

wikipedia = wikipediaapi.Wikipedia('en')
wiki_page = wikipedia.page(f'{month}_{day}')

for section in wiki_page.sections:
  if(section.title == "Events"):
    print_events(section)

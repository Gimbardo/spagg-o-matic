# spagg-o-matic
spagg-o-matic saves from Wikipedia random daily facts, stores them into Redis, and serves them via API

## Requiremens
Just Python3, Pipenv, and Redis

## Getting Started

### Setup
Just setup pipenv:
- pipenv install / pipenv sync

### Host spagg-o-matic
To host spagg-o-matic just launch main.py, via pipenv:
- pipenv run main.py

### Synch Redis
To synch current day to redisDb:
- pipenv run syncher.py

### Cron
You can just use a daily cron ('0 0 * * *') to automatically synch Redis daily

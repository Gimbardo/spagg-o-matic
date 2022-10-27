

[![wakatime](https://wakatime.com/badge/user/cd67ef54-2583-4f5a-9452-9325670c08e5/project/6d60bb4e-ec9c-4389-a852-f704988f0f4b.svg?style=flat)](https://wakatime.com/badge/user/cd67ef54-2583-4f5a-9452-9325670c08e5/project/6d60bb4e-ec9c-4389-a852-f704988f0f4b?style=flat)

# spagg-o-matic
spagg-o-matic saves from Wikipedia random daily facts, stores them into Redis, and serves them via API

## Already hosted by myself:

https://api.gimbaro.dev/daily_fact

## Requiremens
Just Python3, Pipenv, and Redis

---

### Setup

#### without Docker
Just setup pipenv:
- pipenv install / pipenv sync

#### with Docker
- docker compose build

---

### Host spagg-o-matic

#### without Docker
To host spagg-o-matic just launch main.py, via pipenv:
- pipenv run main.py

#### with Docker
- docker compose up

---

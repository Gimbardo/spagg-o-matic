

[![wakatime](https://wakatime.com/badge/user/cd67ef54-2583-4f5a-9452-9325670c08e5/project/6d60bb4e-ec9c-4389-a852-f704988f0f4b.svg?style=flat)](https://wakatime.com/badge/user/cd67ef54-2583-4f5a-9452-9325670c08e5/project/6d60bb4e-ec9c-4389-a852-f704988f0f4b?style=flat)

# spagg-o-matic
spagg-o-matic saves from Wikipedia random daily facts, stores them into Redis, and serves them via API

## Already hosted by myself

https://spaggomatic.gimbaro.dev

## Docs

return example:

```json
{
  "fact": "Just a random Fact",
  "year": "1999"
}

```

## Requirements

Just Python3, Pipenv, and Redis (or Docker and nothing else)

### Setup

#### without Docker

``` shell
  pipenv install
  pipenv run main
```

**NB**: Docker handles cron, to sync 

#### with Docker
``` shell
  docker compose build
  docker compose up
```

---

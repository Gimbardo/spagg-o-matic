from typing import Union
from fastapi import FastAPI
from src.redis_interface import RedisInterface

app = FastAPI()
f = RedisInterface()

@app.get("/ping")
def ping():
  return {"content": "pong"}

@app.get("/daily_fact")
def daily_fact():
  return f.random_fact()
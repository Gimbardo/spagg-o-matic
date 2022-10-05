from typing import Union
from fastapi import FastAPI
from src.redis_interface import RedisInterface
import os

app = FastAPI()
f = RedisInterface(host= os.getenv('REDIS_ADDRESS'))

@app.get("/ping")
def ping():
  return {"content": "pong"}

@app.get("/daily_fact")
def daily_fact():
  return f.random_fact()
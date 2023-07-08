from typing import Union
from fastapi import FastAPI
from src.redis_interface import RedisInterface
from constants import *

app = FastAPI()
f = RedisInterface(host=REDIS_ADDRESS)


@app.get("/ping")
def ping():
    return {"content": "pong"}


@app.get("/")
def daily_fact():
    return f.random_fact()

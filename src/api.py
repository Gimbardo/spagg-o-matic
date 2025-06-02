from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.redis_interface import RedisInterface
from constants import *

origins = [
    "https://gimbaro.dev",
    "http://localhost",
    "http://localhost:63342"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
f = RedisInterface(host=REDIS_ADDRESS)


@app.get("/ping")
def ping():
    return {"content": "pong"}


@app.get("/")
def daily_fact():
    return f.random_fact()

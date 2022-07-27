from typing import Union
from fastapi import FastAPI
from .facterinator import Facterinator

print("test")

app = FastAPI()
f = Facterinator()

@app.get("/ping")
def ping():
  return {"content": "pong"}

@app.get("/daily_fact")
def daily_fact():
  return f.random_fact()
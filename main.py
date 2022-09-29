#!/usr/bin/env python

import asyncio
import uvicorn
from src.api import app
from src.syncher import Syncher
import schedule
import time
import threading

def start_synch():
    while True:
        schedule.run_pending()
        time.sleep(120)

if __name__ == "__main__":
    syncher = Syncher()
    syncher.synch()
    schedule.every().day.at("00:00").do(syncher.synch)
    x = threading.Thread(target=start_synch)
    x.start()
    uvicorn.run(app, port=3000, log_level="info")
    
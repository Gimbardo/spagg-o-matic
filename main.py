#!/usr/bin/env python

import uvicorn
from src.api import app
from src.syncher import Syncher
import schedule
import time
import threading
import os
import logging
def start_synch():
    while True:
        schedule.run_pending()
        time.sleep(int(os.getenv('POLL_INTERVAL')))

if __name__ == "__main__":
    syncher = Syncher()
    syncher.synch()
    schedule.every().day.at("00:00").do(syncher.synch)
    x = threading.Thread(target=start_synch)
    x.start()
    uvicorn.run(app, host='0.0.0.0', port=80, log_level="info")
    
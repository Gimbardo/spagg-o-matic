#!/usr/bin/env python

import uvicorn
from src.api import app
from src.syncher import Syncher
import logging

if __name__ == "__main__":
    syncher = Syncher()
    syncher.synch()
    logging.getLogger().setLevel(logging.INFO)
    uvicorn.run(app, host='0.0.0.0', port=80, log_level="info")

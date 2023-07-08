#!/usr/bin/env python

import uvicorn
from src.api import app
import logging

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    uvicorn.run(app, host='0.0.0.0', port=80, log_level="info")

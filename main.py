#!/usr/bin/env python

import uvicorn
from src.api import app

if __name__ == "__main__":
    uvicorn.run(app, port=8000, log_level="info")
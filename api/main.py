import os
import logging
import sys
from time import sleep
import pytest
import uvicorn
from dotenv import load_dotenv
from logging.config import dictConfig

from config.logConfig import log_config
from app import app

load_dotenv()
HOST = str(os.getenv("HOST"))
PORT = int(os.getenv("PORT"))
DEBBUGING = bool(os.environ.get("DEBBUGING"))

dictConfig(log_config)
logger = logging.getLogger('logger')

server = app


def runServer():
    logger.info('======================================')
    logger.info('========== API RUNNING ...🚀 =========')
    logger.info('======================================')

    uvicorn.run("main:server", host=HOST, port=PORT,
                log_level="info", reload=DEBBUGING)


if __name__ == '__main__':
    runServer()

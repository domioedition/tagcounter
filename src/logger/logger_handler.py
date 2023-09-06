import logging
import os


class LoggerHandler:
    def __init__(self):
        self._logging = logging

        if not os.path.isdir("logs"):
            os.makedirs("logs")

        self._logging.basicConfig(
            level=logging.INFO, filename="logs/py_log.log", filemode="a"
        )

    def info(self, msg):
        self._logging.info(msg)

    def error(self, msg):
        self._logging.error(msg)

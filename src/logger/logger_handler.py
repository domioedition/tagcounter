import logging


class LoggerHandler:
    def __init__(self):
        self._logging = logging

        self._logging.basicConfig(
            level=logging.INFO, filename="py_log.log", filemode="a"
        )

    def info(self, msg):
        self._logging.info(msg)

    def error(self, msg):
        self._logging.error(msg)

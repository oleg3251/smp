# Represents Http exception
import logging


class HttpException(Exception):
    # Http exception constructor
    def __init__(self, message, data=None):
        logging.info('Initialize http exception')
        super().__init__(message)
        self.data = data

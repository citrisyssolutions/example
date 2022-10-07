from loguru import logger

class LogProvider:
    def __init__(self):
        self.logger = logger

    def get_logger(self):
        return self.logger
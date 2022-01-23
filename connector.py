import json
from .logger import Logger

class Connector(Logger):

    def __init__(self, name, debug=False):
        super().__init__(name, debug)
        self.details = json.load(open('configuration/config.json'))
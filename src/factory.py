from config_util import ConfigUtil
from arg_parser import ArgParser
from todo_processor import TodoProcessor
from todo_data import TodoData


class Factory:

    def __init__(self):
        self._config_util = None
        self._arg_parser = None
        self._todo_processor = None
        self._todo_data = None

    def create_config_util(self):
        if (self._config_util == None):
            self._config_util = ConfigUtil()
            return self._config_util
        else:
            return self._config_util
    
    def create_arg_parser(self):
        if (self._arg_parser == None):
            self._arg_parser = ArgParser()
            return self._arg_parser
        else:
            return self._arg_parser

    def create_todo_processor(self):
        if (self._todo_processor == None):
            self._todo_processor = TodoProcessor(self)
            return self._todo_processor
        else:
            return self._todo_processor

    def create_todo_data(self):
        if (self._todo_data == None):
            self._todo_data = TodoData(self)
            return self._todo_data
        else:
            return self._todo_data
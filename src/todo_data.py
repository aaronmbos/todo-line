import json


class TodoData:

    def __init__(self, factory):
        self._factory = factory
        self._config_util = self._factory.create_config_util()
        self._todoFileLocation = self._config_util.get_config_setting('todoFileLocation')

    def create_todo(self, todo_name):
        new_todo = {'title': todo_name}
        with open(self._todoFileLocation, 'w') as file:
            json.dump(new_todo, file)
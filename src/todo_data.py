import json
from models import todo_list

class TodoData:

    def __init__(self, factory):
        self._factory = factory
        self._config_util = self._factory.create_config_util()
        self._todoFileLocation = self._config_util.get_config_setting('todoFileLocation')

    def create_todo(self, todo_name):
        todos = self.get_all_todos()
        new_todo = todo_list.TodoList(todo_name, True, [])
        todos.append(new_todo)
        with open(self._todoFileLocation, 'w') as file:
            json.dump(obj=todos, default=lambda o: o.__dict__, fp=file)

    def get_all_todos(self):
        with open(self._todoFileLocation) as file:
            return json.load(file)
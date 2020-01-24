import json
from models import todo_list
from models import todo_item

class TodoData:

    def __init__(self, factory):
        self._factory = factory
        self._config_util = self._factory.create_config_util()
        self._todoFileLocation = self._config_util.get_config_setting('todoFileLocation')

    def add_todo_item(self, todo_item_desc):
        todos = self.get_all_todos()
        
        for todo in todos:
            if todo.is_active:
                todo.items.append(todo_item.TodoItem(todo_item_desc))
        
        self.write_todos(todos)

    def create_todo(self, todo_name):
        todos = self.get_all_todos()

        # Can't add list with duplicate title
        for todo in todos:
            if todo.title == todo_name:
                raise Exception(f'A list already exists with name: {todo_name}')
        
        new_todo = todo_list.TodoList(todo_name, len(todos) == 0, [])
        todos.append(new_todo)
        self.write_todos(todos)

    def get_active_todo(self):
        for todo in self.get_all_todos():
            if todo.is_active:
                return todo

    def get_all_todos(self):
        with open(self._todoFileLocation) as file:
            jTodos = json.load(file)
            todos = []
            for jTodo in jTodos:
                todo = todo_list.TodoList(jTodo['_title'], jTodo['_is_active'], jTodo['_items'])
                todo.creation_date_time = jTodo['_creation_date_time']
                todo.modified_date_time = jTodo['_modified_date_time']
                todos.append(todo)
            return todos

    def write_todos(self, todos):
        with open(self._todoFileLocation, 'w') as file:
            json.dump(obj=todos, default=lambda o: o.__dict__, fp=file)
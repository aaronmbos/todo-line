import json
import datetime

class TodoData:

    def __init__(self, factory):
        self._factory = factory
        self._config_util = self._factory.create_config_util()
        self._todoFileLocation = self._config_util.get_config_setting('todoFileLocation')

    def add_todo_item(self, todo_item_desc):
        todos = self.get_all_todos()
        
        for todo in todos:
            if todo['is_active']:
                todo['items'].append({'desc': todo_item_desc, 'status': 'incomplete', 'date_created': str(datetime.datetime.now())})
        
        self.write_todos(todos)

    def create_todo(self, todo_name):
        todos = self.get_all_todos()

        # Can't add list with duplicate title
        for todo in todos:
            if todo['title'] == todo_name:
                raise Exception(f'A list already exists with name: {todo_name}')
        new_todo = {'title': todo_name, 'items': [], 'is_active': len(todos) == 0, 'date_created': str(datetime.datetime.now()), 'date_mod': str(datetime.datetime.now())}
        todos.append(new_todo)
        self.write_todos(todos)

    def get_active_list_items(self):
        for todo in self.get_all_todos():
            if todo['is_active']:
                return todo['items']

    def get_active_todo(self):
        for todo in self.get_all_todos():
            if todo['is_active']:
                return todo

    def get_all_todos(self):
        with open(self._todoFileLocation) as file:
            return json.load(file)

    def check_todo_item(self, item_idx):
        all_todos = self.get_all_todos()
        updated_item = None
        
        for _todo in all_todos:
            if _todo['is_active']:
                for index, _item in enumerate(_todo['items']):
                    if index == item_idx:
                        _item['status'] = 'completed'
                        updated_item = _item
                        break
                _todo['date_mod'] = str(datetime.datetime.now())
                break

        self.write_todos(all_todos)
        return updated_item

    def write_todos(self, todos):
        with open(self._todoFileLocation, 'w') as file:
            json.dump(todos, fp=file)
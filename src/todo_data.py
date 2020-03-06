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
                todo['items'].append({'desc': todo_item_desc, 'status': 'incomplete','sub_items': [], 'date_created': str(datetime.datetime.now())})
        
        self.write_todos(todos)

    def add_todo_sub_item(self, todo_sub_item_desc, sub_place):
        all_todos = self.get_all_todos()
        for todo in all_todos:
            if todo['is_active']:
                for index, item in enumerate(todo['items']):
                    if index == sub_place - 1:
                        item['sub_items'].append({'desc': todo_sub_item_desc, 'status': 'incomplete','sub_items': [], 'date_created': str(datetime.datetime.now())})
                        break
                todo['date_mod'] = str(datetime.datetime.now())
                break
        self.write_todos(all_todos)

    def create_todo(self, todo_name):
        todos = self.get_all_todos()

        # Can't add list with duplicate title
        for todo in todos:
            if todo['title'] == todo_name:
                raise Exception(f'A list already exists with name: {todo_name}')
        new_todo = {'title': todo_name, 'items': [], 'is_active': len(todos) == 0, 'date_created': str(datetime.datetime.now()), 'date_mod': str(datetime.datetime.now())}
        todos.append(new_todo)
        self.write_todos(todos)

    def get_active_todo(self):
        for todo in self.get_all_todos():
            if todo['is_active']:
                return todo

    def get_all_todos(self):
        with open(self._todoFileLocation) as file:
            return json.load(file)

    def update_todo_item_status(self, item_idx, status):
        all_todos = self.get_all_todos()
        updated_item = None
        
        for todo in all_todos:
            if todo['is_active']:
                for index, _item in enumerate(todo['items']):
                    if index == item_idx:
                        _item['status'] = status
                        updated_item = _item
                        break
                todo['date_mod'] = str(datetime.datetime.now())
                break
        # Only write to file if we updated item
        if updated_item:
            self.write_todos(all_todos)
        return updated_item

    def update_sub_item_status(self, item_idx, sub_idx, status):
        all_todos = self.get_all_todos()
        updated_sub = None

        for todo in all_todos:
            if todo['is_active']:
                for index, item in enumerate(todo['items']):
                    if index == item_idx:
                        sub = item['sub_items'][sub_idx]
                        sub['status'] = status
                        updated_sub = sub
                        break
                todo['date_mod'] = str(datetime.datetime.now())
                break
        if updated_sub:
            self.write_todos(all_todos)
        return updated_sub
    
    def checkout_todo(self, idx):
        all_todos = self.get_all_todos()
        checkedout_todo = None
        
        for index, _todo in enumerate(all_todos):
            if index == idx:
                _todo['is_active'] = True
                checkedout_todo = _todo
            else:
                _todo['is_active'] = False
        
        # Only write to file if a todo was able to be checked out
        if checkedout_todo:
            self.write_todos(all_todos)
        return checkedout_todo

    def delete_todo(self, idx):
        all_todos = self.get_all_todos()
        try:
            del all_todos[idx]
            self.write_todos(all_todos)
            return True
        except Exception:
            return False

    def delete_todo_item(self, idx):
        all_todos = self.get_all_todos()
        is_deleted = False
        for todo in all_todos:
            if todo['is_active']:
                try:
                    del todo['items'][idx]
                    todo['date_mod'] = str(datetime.datetime.now())
                    is_deleted = True
                except Exception:
                    is_deleted = False
                break
        
        self.write_todos(all_todos)
        return is_deleted

    def update_todo(self, idx, title):
        all_todos = self.get_all_todos()
        try:
            todo = all_todos[idx]
            todo['title'] = title
            todo['date_mod'] = str(datetime.datetime.now())
            self.write_todos(all_todos)
            return True
        except IndexError:
            return False

    def update_todo_item(self, idx, desc):
        all_todos = self.get_all_todos()
        for todo in all_todos:
            if todo['is_active']:
                try:
                    todo['items'][idx]['desc'] = desc
                    todo['date_mod'] = str(datetime.datetime.now())
                except IndexError:
                    return False
                break
        self.write_todos(all_todos)
        return True

    def insert_todo(self, idx, title):
        all_todos = self.get_all_todos()
        try:
            all_todos.insert(idx, {'title': title, 'items': [], 'is_active': len(all_todos) == 0, 'date_created': str(datetime.datetime.now()), 'date_mod': str(datetime.datetime.now())})
            self.write_todos(all_todos)
            return True
        except IndexError:
            return False

    def insert_todo_item(self, idx, desc):
        all_todos = self.get_all_todos()
        for todo in all_todos:
            if todo['is_active']:
                try:
                    todo['items'].insert(idx, {'desc': desc, 'status': 'incomplete', 'date_created': str(datetime.datetime.now())})
                except IndexError:
                    return False
                break
        self.write_todos(all_todos)
        return True

    def write_todos(self, todos):
        with open(self._todoFileLocation, 'w') as file:
            json.dump(todos, fp=file)
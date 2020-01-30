from todo_data import TodoData

class TodoProcessor:

    def __init__(self, factory):
        self._factory = factory
        self._todo_data = self._factory.create_todo_data()

    def create_new_todo(self, todo_name):
        if self.validate_todo(todo_name):
            try:
                self._todo_data.create_todo(todo_name)
                print(f'\nTodo created successfully!')
                self.list_todos()
            except Exception as ex:
                print(f'\n{str(ex)}\n')
        else:
            print('Todo name must be greater than 0 and less than 100 chars')

    def add_todo_item(self, todo_item_desc):
        if self.validate_todo_item(todo_item_desc):
            self._todo_data.add_todo_item(todo_item_desc)
            print(f'\nItem added successfully!')
            self.list_todo_items()
        else:
            print('Todo item description must be greater than 0 and less than 100 chars')

    def get_list(self, list_type):
        if list_type == 'items' or list_type == 'item':
            self.list_todo_items()
        elif list_type == 'todos' or list_type == 'todo':
            self.list_todos()
        else:
            print(f'{list_type} is not a recognized list type')

    def list_todos(self):
        _todos = self._todo_data.get_all_todos()
        formatted_todos = f'\n'
        for idx, _todo in enumerate(_todos):
            formatted_todos += f'{idx + 1}. {_todo["title"]}{"*" if _todo["is_active"] else ""}\n'
        
        print(formatted_todos)

    def list_todo_items(self):
        _todo = self._todo_data.get_active_todo()
        formatted_items = f'\nItems in {_todo["title"]}:\n'
        for idx, _item in enumerate(_todo['items']):
            formatted_items += f'{idx + 1}. [ {"x" if _item["status"] == "completed" else "o"} ] {_item["desc"]}\n'
        
        print(formatted_items)

    def validate_todo(self, todo_name):
        if len(todo_name) == 0 or len(todo_name) > 100:
            return False
        return True

    def validate_todo_item(self, item_desc):
        if len(item_desc) == 0 or len(item_desc) > 100:
            return False
        return True

    def check_todo_item(self, rawArg):
        try:
            _item_idx = int(rawArg) - 1
            _item = self._todo_data.update_todo_item_status(_item_idx, 'completed')
            if _item:
                print(f'{rawArg}. {_item["desc"]} is completed')
            else:
                print(f'Unable to complete requested item: {rawArg}')
        except ValueError:
            print('Argument with ch command must be an integer')

    def uncheck_todo_item(self, rawArg):
        try:
            _item_idx = int(rawArg) - 1
            _item = self._todo_data.update_todo_item_status(_item_idx, 'incomplete')
            if _item:
                print(f'{rawArg}. {_item["desc"]} is marked incomplete')
            else:
                print(f'Unable to mark requested item incomplete: {rawArg}')
        except ValueError:
            print('Argument with ch command must be an integer')

    def checkout_todo(self, rawIdx):
        try:
            idx = int(rawIdx) - 1
            _todo = self._todo_data.checkout_todo(idx)
            if _todo:
                print(f'{_todo["title"]} checked out successfully')
            else:
                print(f'Unable to checkout todo number {rawIdx}')
        except ValueError:
            print('Argument with checkout command must be an integer')

    def process_todo(self, args):
        if args.new:
            self.create_new_todo(args.new)
        elif args.add:
            self.add_todo_item(args.add)
        elif args.check:
            self.check_todo_item(args.check)
        elif args.checkout:
            self.checkout_todo(args.checkout)
        elif args.uncheck:
            self.uncheck_todo_item(args.uncheck)
        elif args.remove:
            pass
        elif args.list:
            self.get_list(args.list)
        else:
            pass
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
        todos = self._todo_data.get_all_todos()
        formatted_todos = f'\n'
        for idx, todo in enumerate(todos):
            formatted_todos += f'{idx + 1}. {todo["title"]}{"*" if todo["is_active"] else ""}\n'
        
        print(formatted_todos)

    def list_todo_items(self):
        todo = self._todo_data.get_active_todo()
        formatted_items = f'\nItems in {todo["title"]}:\n'
        for idx, item in enumerate(todo['items']):
            formatted_items += f'{idx + 1}. [ {"x" if item["status"] == "completed" else "o"} ] {item["desc"]}\n'
        
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
            item_idx = int(rawArg) - 1
            item = self._todo_data.update_todo_item_status(item_idx, 'completed')
            if item:
                print(f'{rawArg}. {item["desc"]} is completed')
            else:
                print(f'Unable to complete requested item: {rawArg}')
        except ValueError:
            print('Argument with ch command must be an integer')

    def uncheck_todo_item(self, rawArg):
        try:
            item_idx = int(rawArg) - 1
            item = self._todo_data.update_todo_item_status(item_idx, 'incomplete')
            if item:
                print(f'{rawArg}. {item["desc"]} is marked incomplete')
            else:
                print(f'Unable to mark requested item incomplete: {rawArg}')
        except ValueError:
            print('Argument with ch command must be an integer')

    def checkout_todo(self, rawIdx):
        try:
            idx = int(rawIdx) - 1
            todo = self._todo_data.checkout_todo(idx)
            if todo:
                print(f'{todo["title"]} checked out successfully')
            else:
                print(f'Unable to checkout todo number {rawIdx}')
        except ValueError:
            print('Argument with checkout command must be an integer')
    
    def delete(self, delete_Arg, raw_Idx):
        is_deleted = False
        delete_type = ''
        try:
            idx = int(raw_Idx) - 1
            if delete_Arg.lower() == 'todo' or delete_Arg.lower() == 'todos':
                delete_type = 'todo'
                is_deleted = self._todo_data.delete_todo(idx)
            elif delete_Arg.lower() == 'item' or delete_Arg.lower() == 'items':
                delete_type = 'item'
                is_deleted = self._todo_data.delete_todo_item(idx)
            else:
                print(f'Unrecognized delete argument: {delete_Arg}')
                return
        except ValueError:
            print('Index argument must be an integer')

        if is_deleted:
            print(f'{delete_type} deleted successfully')
        else:
            print(f'Unable to delete {delete_type} at index {raw_Idx}')
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
        elif args.delete:
            if not args.index:
                print('Unable to process request: --index is a required argument with delete command')
            self.delete(args.delete, args.index)
        elif args.list:
            self.get_list(args.list)
        else:
            pass
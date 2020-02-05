from todo_data import TodoData

class TodoProcessor:
    _todo_validation_message = 'Todo title must be greater than 0 and less than 100 chars'
    _todo_item_validation_message = 'Todo item description must be greater than 0 and less than 100 chars'
    _index_validation_message = 'Index argument must be an integer'

    def __init__(self, factory):
        self._factory = factory
        self._todo_data = self._factory.create_todo_data()

    def create_new_todo(self, todo_name):
        if self.validate_todo(todo_name):
            try:
                self._todo_data.create_todo(todo_name)
                print(f'Todo created successfully')
                self.list_todos()
            except Exception as ex:
                print(f'{str(ex)}')
        else:
            print(self._todo_validation_message)

    def add_todo_item(self, todo_item_desc):
        if self.validate_todo_item(todo_item_desc):
            self._todo_data.add_todo_item(todo_item_desc)
            print(f'Item added successfully')
            self.list_todo_items()
        else:
            print(self._todo_item_validation_message)

    def get_list(self, list_type):
        if self.is_item_request(list_type):
            self.list_todo_items()
        elif self.is_todo_request(list_type):
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
            formatted_items += f'[{"x" if item["status"] == "completed" else " "}] {idx + 1}. {item["desc"]}\n'
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
            if self.is_todo_request(delete_Arg):
                delete_type = 'todo'
                is_deleted = self._todo_data.delete_todo(idx)
            elif self.is_item_request(delete_Arg):
                delete_type = 'item'
                is_deleted = self._todo_data.delete_todo_item(idx)
            else:
                print(f'Unrecognized delete argument: {delete_Arg}')
                return
        except ValueError:
            print(self._index_validation_message)

        if is_deleted:
            print(f'{delete_type} deleted successfully')
        else:
            print(f'Unable to delete {delete_type} at index {raw_Idx}')
    
    def update(self, update_arg, idx_arg, content_arg):
        try:
            index = int(idx_arg) - 1
            if self.is_todo_request(update_arg):
                if self.validate_todo(content_arg):
                    if self._todo_data.update_todo(index, content_arg):
                        print('Todo updated successfully')
                    else:
                        print(f'Unable to update todo at index: {idx_arg}')
                else:
                    print(self._todo_validation_message)
            elif self.is_item_request(update_arg):
                if self.validate_todo_item(content_arg):
                    if self._todo_data.update_todo_item(index, content_arg):
                        print('Todo item updated successfully')
                    else:
                        print(f'Unable to update todo item at index: {idx_arg}')
                else:
                    print(self._todo_item_validation_message)
            else:
                print('Unable to process request due to unrecognized update argument')
                return
        except ValueError:
            print(self._index_validation_message)

    def is_todo_request(self, req_arg):
        if req_arg.lower() == 'todo' or req_arg.lower() == 'todos':
            return True 
        return False

    def is_item_request(self, req_arg):
        if req_arg.lower() == 'item' or req_arg.lower() == 'items':
            return True 
        return False

    def insert(self, insert_arg, idx_arg, value_arg):
        try:
            index = int(idx_arg) - 1
            if self.is_todo_request(insert_arg):
                if self._todo_data.insert_todo(index, value_arg):
                    print(f'Todo inserted at index: {idx_arg}')
                else:
                    print(f'Unable to insert todo at index: {idx_arg}')
            elif self.is_item_request(insert_arg):
                if self._todo_data.insert_todo_item(index, value_arg):
                    print(f'Todo item inserted at index: {idx_arg}')
                else:
                    print(f'Unable to insert todo item at index: {idx_arg}')
            else:
                print('Unable to process request due to unrecognized insert argument')
        except ValueError:
            print(self._index_validation_message)

    def process_new_todo(self, args):
        if args.new:
            self.create_new_todo(args.new)

    def process_add_todo_item(self, args):
        if args.add:
            self.add_todo_item(args.add)
            
    def process_todo(self, args):
        if args.check:
            self.check_todo_item(args.check)
        elif args.checkout:
            self.checkout_todo(args.checkout)
        elif args.uncheck:
            self.uncheck_todo_item(args.uncheck)
        elif args.delete:
            if not args.index:
                print('Unable to process request: --index is a required argument with delete command')
                return
            self.delete(args.delete, args.index)
        elif args.insert:
            if not args.index or not args.value:
                print('Unable to process request: --index and --value are required arguments with update command')
                return
            self.insert(args.insert, args.index, args.value)
        elif args.list:
            self.get_list(args.list)
        elif args.update:
            if not args.index or not args.value:
                print('Unable to process request: --index and --value are required arguments with update command')
                return
            self.update(args.update, args.index, args.value)    
        else:
            pass
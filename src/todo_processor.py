from todo_data import TodoData
import datetime

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
        if len(todos) > 0:
            formatted_todos = f'\n'
            for idx, todo in enumerate(todos):
                formatted_todos += f'{idx + 1}. {todo["title"]}{"*" if todo["is_active"] else ""}\n'
            print(formatted_todos)
        else:
            print('There are no existing todo lists')

    def list_todo_items(self):
        todo = self._todo_data.get_active_todo()
        if len(todo['items']) > 0:
            formatted_items = f'\nItems in {todo["title"]}:\n'
            for idx, item in enumerate(todo['items']):
                formatted_items += f'[{"x" if item["status"] == "completed" else " "}] {idx + 1}. {item["desc"]}\n'
                if len(item['sub_items']) > 0:
                    for index, sub in enumerate(item['sub_items']):
                        formatted_items += f'    [{"x" if sub["status"] == "completed" else " "}] {index + 1}. {sub["desc"]}\n'
            print(formatted_items)
        else:
            print(f'There are no items in {todo["title"]}')
        

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
            print('Argument with uncheck command must be an integer')

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
    def delete_sub_item(self, delete_arg, sub_place, delete_place):
        is_deleted = False
        try:
            if self.is_todo_request(delete_arg):
                print('Action not supported. delete todo cannot be used with --sub')
            else:
                is_deleted = self._todo_data.delete_sub_item(delete_place - 1, sub_place - 1)
        except Exception:
            is_deleted = False

        if is_deleted:
            print('Sub item delete successfully')
        else:
            print('Unable to delete sub item')

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
            print(f'Unable to delete {delete_type} at place {raw_Idx}')
    
    def update(self, update_arg, idx_arg, content_arg):
        try:
            index = int(idx_arg) - 1
            if self.is_todo_request(update_arg):
                if self.validate_todo(content_arg):
                    if self._todo_data.update_todo(index, content_arg):
                        print('Todo updated successfully')
                    else:
                        print(f'Unable to update todo at place: {idx_arg}')
                else:
                    print(self._todo_validation_message)
            elif self.is_item_request(update_arg):
                if self.validate_todo_item(content_arg):
                    if self._todo_data.update_todo_item(index, content_arg):
                        print('Todo item updated successfully')
                    else:
                        print(f'Unable to update todo item at place: {idx_arg}')
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
                    print(f'Todo inserted at place: {idx_arg}')
                else:
                    print(f'Unable to insert todo at place: {idx_arg}')
            elif self.is_item_request(insert_arg):
                if self._todo_data.insert_todo_item(index, value_arg):
                    print(f'Todo item inserted at place: {idx_arg}')
                else:
                    print(f'Unable to insert todo item at place: {idx_arg}')
            else:
                print('Unable to process request due to unrecognized insert argument')
        except ValueError:
            print(self._index_validation_message)

    def add_sub_item(self, add_arg, place_arg):
        if not place_arg:
            print('-p/--place argument is required for adding sub items')
        else:
            self._todo_data.add_todo_sub_item(add_arg, place_arg)
            print('Todo sub item added successfully.')
            self.list_todo_items()

    def check_sub_item(self, check_arg, place_arg):
        if not place_arg:
            print('-p/--place argument is require for checking sub items')
        else:
            updated = self._todo_data.update_sub_item_status(int(check_arg) - 1, place_arg - 1, 'completed')
            if updated:
                print(f'{updated["desc"]} checked successfully')
            else:
                print(f'Unable to check todo sub item {updated["desc"]}')

    def uncheck_sub_item(self, check_arg, place_arg):
        if not place_arg:
            print('-p/--place argument is require for checking sub items')
        else:
            updated = self._todo_data.update_sub_item_status(int(check_arg) - 1, place_arg - 1, 'incomplete')
            if updated:
                print(f'{updated["desc"]} unchecked successfully')
            else:
                print(f'Unable to uncheck todo sub item {updated["desc"]}')

    def update_sub_item(self, update_arg, place_arg, val_arg, sub_arg):
        if self.is_todo_request(update_arg):
            print('Action not supported. update todo cannot be used with --sub option')
        else:
            updated = self._todo_data.update_sub_item(int(place_arg) - 1, sub_arg - 1, val_arg)

        if updated:
            pass
        else:
            pass

    def process_new_todo(self, args):
        self.create_new_todo(args.new)

    def process_add_todo_item(self, args):
        if args.sub == -1:
            self.add_todo_item(args.add)
        else:
            self.add_sub_item(args.add, args.sub)

    def process_check_todo_item(self, args):
        if args.sub == -1:
            self.check_todo_item(args.check)
        else:
            self.check_sub_item(args.check, args.sub)

    def process_get_list(self, args):
        self.get_list(args.list)

    def process_checkout(self, args):
        self.checkout_todo(args.checkout)

    def process_uncheck(self, args):
        if args.sub != -1:
            self.uncheck_sub_item(args.uncheck, args.sub)
        else:
            self.uncheck_todo_item(args.uncheck)

    def process_delete(self, args):
        if not args.place:
                print('Unable to process request: -p/--place is a required argument with delete command')
                return
        if args.sub != -1:
            self.delete_sub_item(args.delete, args.sub, args.place)
        else:
            self.delete(args.delete, args.place)

    def process_insert(self, args):
        if not args.place or not args.value:
            print('Unable to process request: --index and --value are required arguments with update command')
            return
        self.insert(args.insert, args.place, args.value)

    def process_update(self, args):
        if not args.place or not args.value:
            print('Unable to process request: --index and --value are required arguments with update command')
            return
        if args.sub == -1:
            self.update(args.update, args.place, args.value)
        else:
            self.update_sub_item(args.update, args.place, args.value, args.sub)
            
from todo_data import TodoData

class TodoProcessor:

    def __init__(self, factory):
        self._factory = factory
        self._todo_data = self._factory.create_todo_data()

    def create_new_todo(self, todo_name):
        self._todo_data.create_todo(todo_name)
        print(f'Todo created successfully!')

    def add_todo_item(self, todo_item_desc):
        self._todo_data.add_todo_item(todo_item_desc)
        print(f'\nItem added successfully!')
        self.list_items()

    def list_items(self):
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

    def process_todo(self, args):
        if args.new:
            if self.validate_todo(args.new):
                self.create_new_todo(args.new)
            else:
                print('Todo name must be greater than 0 and less than 100 chars')
        elif args.add:
            if self.validate_todo_item(args.add):
                self.add_todo_item(args.add)
            else:
                print('Todo item description must be greater than 0 and less than 100 chars')
        elif args.ch:
            try:
                _item_idx = int(args.ch) - 1
                _item = self._todo_data.check_todo_item(_item_idx)
                if _item:
                    print(f'{args.ch}. {_item["desc"]} is completed')
                else:
                    print(f'Unable to complete requested item: {args.ch}')
            except ValueError:
                print('Argument with ch command must be an integer')
        elif args.rem:
            pass
        elif args.list or args.l:
            self.list_items()
        else:
            pass
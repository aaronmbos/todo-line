from todo_data import TodoData

class TodoProcessor:

    def __init__(self, factory):
        self._factory = factory
        self._todo_data = self._factory.create_todo_data()

    def create_new_todo(self, todo_name):
        self._todo_data.create_todo(todo_name)

    def add_todo_item(self, todo_item_desc):
        self._todo_data.add_todo_item(todo_item_desc)

    def list_items(self):
        self._todo_data.get_active_list_items()

    def process_todo(self, args):
        if args.new:
            self.create_new_todo(args.new)
        elif args.add:
            self.add_todo_item(args.add)
        elif args.rem:
            pass
        elif args.list or args.l:
            self.list_items()
        else:
            pass
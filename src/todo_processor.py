from todo_data import TodoData

class TodoProcessor:

    def __init__(self, factory):
        self._factory = factory
        self._todo_data = self._factory.create_todo_data()

    def create_new_todo(self, todo_name):
        self._todo_data.create_todo(todo_name)

    def process_todo(self, args):
        if args.new:
            self.create_new_todo(args.new)
        elif args.rem:
            pass
        else:
            pass
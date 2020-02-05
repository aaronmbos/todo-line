import argparse

class ArgParser:

    def __init__(self, factory): 
        self._factory = factory
        self._todo_processor = self._factory.create_todo_processor()

    def process_todo_request(self):
        parsed_args = self.parse_args()
        parsed_args.func(parsed_args)

    def parse_args(self):
        parser = argparse.ArgumentParser(description='A todo list for your command line')
        subparsers = parser.add_subparsers()

        new_cmd = subparsers.add_parser('new', help='Create a new todo list')
        new_cmd.add_argument('new')
        new_cmd.set_defaults(func=self._todo_processor.process_new_todo)

        add_cmd = subparsers.add_parser('add', help='Add a todo item to list')
        add_cmd.add_argument('add')
        add_cmd.set_defaults(func=self._todo_processor.process_add_todo_item)

        parser.add_argument('--delete', help='Delete a todo list or item. Require sub-argument(s): --index')
        parser.add_argument('--checkout', help='Checkout todo list')
        parser.add_argument('--insert', help='Insert a todo list or item to list. Required sub-argument(s): --index, --value')
        parser.add_argument('--update', help='Update a todo item in list. Required sub-argument(s): --index, --value')
        parser.add_argument('--check', help='Check an item off list based on order')
        parser.add_argument('--uncheck', help='Uncheck an item on list based on order')
        parser.add_argument('--value', help='Sub-argument that can be used with other commands i.e. --update')
        parser.add_argument('--index', help='One based index of todo list or item')
        parser.add_argument('--list', help='List items in active todo list or all todo lists')
        return parser.parse_args()
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
        self.add_all_subparsers(parser)
        return parser.parse_args()
    
    def add_all_subparsers(self, parser):
        subparsers = parser.add_subparsers()

        new_cmd = subparsers.add_parser('new', help='Create a new todo list')
        new_cmd.add_argument('new')
        new_cmd.set_defaults(func=self._todo_processor.process_new_todo)

        add_cmd = subparsers.add_parser('add', help='Add a todo item to list')
        add_cmd.add_argument('add')
        add_cmd.add_argument('-s', '--sub', action='store_true')
        add_cmd.add_argument('-p', '--place', type=int, help='Argument corresponding to the place of an item for which to add sub item')
        add_cmd.set_defaults(func=self._todo_processor.process_add_todo_item)

        check_cmd = subparsers.add_parser('check', help='Check an item off list based on place')
        check_cmd.add_argument('check')
        check_cmd.add_argument('-s', '--sub', action='store_true')
        check_cmd.add_argument('-p', '--place', type=int, help='Argument corresponding to place of the sub item')
        check_cmd.set_defaults(func=self._todo_processor.process_check_todo_item)

        list_cmd = subparsers.add_parser('list', help='List items in active todo list or all todo lists')
        list_cmd.add_argument('list')
        list_cmd.set_defaults(func=self._todo_processor.process_get_list)

        checkout_cmd = subparsers.add_parser('checkout', help='Checkout todo list based on place')
        checkout_cmd.add_argument('checkout')
        checkout_cmd.set_defaults(func=self._todo_processor.process_checkout)

        uncheck_cmd = subparsers.add_parser('uncheck', help='Uncheck an item on list based on order')
        uncheck_cmd.add_argument('uncheck')
        check_cmd.add_argument('-s', '--sub', action='store_true')
        check_cmd.add_argument('-p', '--place', type=int, help='Argument corresponding to place of the sub item')
        uncheck_cmd.set_defaults(func=self._todo_processor.process_uncheck)

        delete_cmd = subparsers.add_parser('delete', help='Delete a todo list or item. Required argument(s): -p/--place')
        delete_cmd.add_argument('delete')
        delete_cmd.add_argument('-p', '--place', help='Argument corresponding to the place of an item in a todo list or a todo in all todos')
        delete_cmd.set_defaults(func=self._todo_processor.process_delete)

        insert_cmd = subparsers.add_parser('insert', help='Insert a todo list or item to list. Required argument(s): -p/--place, -v/--value')
        insert_cmd.add_argument('insert')
        insert_cmd.add_argument('-p', '--place', help='Argument corresponding to the place of an item in a todo list or a todo in all todos')
        insert_cmd.add_argument('-v', '--value', help='Argument corresponding to the value or a todo or todo item')
        insert_cmd.set_defaults(func=self._todo_processor.process_insert)

        update_cmd = subparsers.add_parser('update', help='Update a todo item in list. Required argument(s): -p/--place, -v/--value')
        update_cmd.add_argument('update')
        update_cmd.add_argument('-p', '--place', help='Argument corresponding to the place of an item in a todo list or a todo in all todos')
        update_cmd.add_argument('-v', '--value', help='Argument corresponding to the value or a todo or todo item')
        update_cmd.set_defaults(func=self._todo_processor.process_update)
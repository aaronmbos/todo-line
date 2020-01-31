import argparse


class ArgParser:

    def __init__(self): 
        pass

    def parse_args(self):
        parser = argparse.ArgumentParser(description='A todo list for your command line')
        parser.add_argument('todo', default='todo')
        parser.add_argument('--new', help='Create a new todo list')
        parser.add_argument('--delete', help='Delete a todo list')
        parser.add_argument('--checkout', help='Checkout todo list')
        parser.add_argument('--add', help='Add a todo item to list')
        parser.add_argument('--insert', help='Insert a todo item to list')
        parser.add_argument('--update', help='Update a todo item in list')
        parser.add_argument('--check', help='Check an item off list based on order')
        parser.add_argument('--uncheck', help='Uncheck an item on list based on order')
        parser.add_argument('--title', help='Title of the todo list')
        parser.add_argument('-d', '--desc', help='Todo list item description')
        parser.add_argument('--index', help='One based index of todo list or item')
        parser.add_argument('--list', help='List items in active todo list or all todo lists')
        return parser.parse_args()
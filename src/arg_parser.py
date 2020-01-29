import argparse


class ArgParser:

    def __init__(self): 
        pass

    def parse_args(self):
        parser = argparse.ArgumentParser(description='A todo list for your command line')
        parser.add_argument('todo', default='todo')
        parser.add_argument('--new', help='Create a new todo list')
        parser.add_argument('--delete', help='Delete a todo list')
        parser.add_argument('--activate', help='Set active todo list')
        parser.add_argument('--add', help='Add a todo item to list')
        parser.add_argument('--insert', help='Insert a todo item to list')
        parser.add_argument('--update', help='Update a todo item in list')
        parser.add_argument('--remove', help='Remove an item from list')
        parser.add_argument('--check', help='Check an item off list based on order')
        parser.add_argument('--uncheck', help='Uncheck an item on list based on order')
        parser.add_argument('-t', '--title', help='Title of the todo list')
        parser.add_argument('-d', '--desc', help='Todo list item description')
        parser.add_argument('-i', '--index', help='Zero based list item index')
        parser.add_argument('-l', '--list', action='store_true', help='List items in active todo list')
        return parser.parse_args()
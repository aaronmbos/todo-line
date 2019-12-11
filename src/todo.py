import argparse
from factory import Factory

if __name__ == "__main__":
    # _factory = Factory()
    # _factory.config_util_create().get_or_set()
    parser = argparse.ArgumentParser(description='A todo list for your command line')
    parser.add_argument('--new', help='Create a new todo list', const='new', nargs='?')
    parser.add_argument('--del', help='Delete a todo list', required=False)
    parser.add_argument('--set', help='Set active todo list')
    parser.add_argument('--add', help='Add a todo item to list')
    parser.add_argument('--ins', help='Insert a todo item to list')
    parser.add_argument('--upd', help='Update a todo item in list')
    parser.add_argument('--rem', help='Remove an item from list')
    parser.add_argument('-t', '--title', help='Title of the todo list')
    parser.add_argument('-l', '--list', help='Todo list item content')
    parser.add_argument('-i', '--index', help='Zero based list item index')
    args = parser.parse_args()
    test = args
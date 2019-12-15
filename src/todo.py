import argparse
from factory import Factory

if __name__ == "__main__":
    _factory = Factory()

    parsed_args = _factory.create_arg_parser().parse_args()
    _factory.create_todo_processor().process_todo(parsed_args)
import argparse
from factory import Factory

if __name__ == "__main__":
    _factory = Factory()
    # _factory.config_util_create().get_or_set()
    parsed_args = _factory.create_arg_parser().parse_args()
    _factory.create_todo_processor().process_todo(parsed_args)
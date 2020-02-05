import argparse
from factory import Factory

if __name__ == "__main__":
    _factory = Factory() 

    parsed_args = _factory.create_arg_parser().process_todo_request()
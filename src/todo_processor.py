class TodoProcessor:

    def __init__(self, factory):
        self._factory = factory


    def create_new_todo(self, todoName):
        config_util = self._factory.create_config_util()


    def process_todo(self, args):
        if args.new:
            self.create_new_todo(args.new)
        elif args.rem:
            pass
        else:
            pass
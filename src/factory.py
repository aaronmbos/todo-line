from config_util import ConfigUtil


class Factory:

    def __init__(self):
        self._config_util = None


    def config_util_create(self):
        if (self._config_util == None):
            self._config_util = ConfigUtil()
            return self._config_util
        else:
            return self._config_util
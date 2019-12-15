from pathlib import Path
from pathlib import os
import json


class ConfigUtil:
    _config_file_name = 'config.json'

    def __init__(self):
        pass

    def get_config_path(self):
        if os.name == 'posix':
            return f'{Path.home()}/Applications/Pytodo/configs'

    def get_or_set_config(self):
        config_path = self.get_config_path()
        path = Path(config_path)
        if not path.exists():
            path.mkdir()
        return path.__str__()

    def get_config_setting(self, key):
        with open(f'{self.get_config_path()}/{self._config_file_name}', 'r') as config_file:
            json_config = json.load(config_file)
            # add exception handling if key isn't found
            return json_config[key]
        
        


from pathlib import Path
from pathlib import os


class ConfigUtil:
    _config_dir_name = 'pytodo_config'
    _config_file_name = 'pytodo.json'


    def __init__(self):
        pass


    def get_config_path(self):
        if os.name == 'posix':
            return f'{Path.home()}/Applications/Pytodo/configs'


    def get_or_set(self):
        config_path = self.get_config_path()
        path = Path(config_path)
        if not path.exists():
            path.mkdir()
        else:
            pass
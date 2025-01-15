import json
from pathlib import Path


class DatabaseConfigLoader:
    def __init__(self, path):
        self.path = path

    def load(self, env, extend_dict=None):
        if extend_dict is None:
            extend_dict = {}
        file_name = self.path / f"database.{env}.json"
        with open(file_name, 'r') as fd:
            config = json.load(fd)
            for key, value in config.items():
                if key == 'extend':
                    self.load(config[key], extend_dict)
                else:
                    extend_dict[key] = value
        return extend_dict


p = Path('2-hexlet-git')
path = p / 'polymorfizm' / 'disp_file' / 'fixtures'
loader = DatabaseConfigLoader(path)
config = loader.load('custom')
print(config)

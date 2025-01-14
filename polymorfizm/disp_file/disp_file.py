import json
from pathlib import Path


class DatabaseConfigLoader:
    def __init__(self, path):
        self.path = path

    def load(self, env):
        file_name = f"database.{env}.json"
        with open(file_name, 'r') as fd:
            config = json.load(fd)
        return config


p = Path('/2-hexlet-git')
path = p / 'polymorfizm' / 'disp_file' / 'fixtures'
loader = DatabaseConfigLoader(path)
config = loader.load('custom')
print(config)

## {
##   host: 'google.com',
##   username: 'postgres',
## };

import yaml


class YAMLParser:

    def __init__(self, data):
        self.data = data

    def get_parse(self):
        return yaml.safe_load(self.data)
# END

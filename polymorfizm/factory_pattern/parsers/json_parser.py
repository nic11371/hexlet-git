import json


class JSONParser:

    def __init__(self, data):
        self.data = data

    def get_parse(self):
        result = json.loads(self.data)
        return result

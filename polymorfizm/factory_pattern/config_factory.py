import os
from polymorfizm.factory_pattern.parsers.json_parser import JSONParser
from polymorfizm.factory_pattern.parsers.yaml_parser import YAMLParser
from polymorfizm.factory_pattern.config_klass import Config


PARSERS = {
    '.yaml': YAMLParser,
    '.yml': YAMLParser,
    '.json': JSONParser,
}


# BEGIN (write your solution here)
class ConfigFactory:

    def factory(path):
        with open(path) as file:
            data = file.read()
            path_file, ext = os.path.splitext(path)
            if ext in PARSERS:
                parser = PARSERS[ext](data)
                return Config(parser.get_parse())
            else:
                raise ValueError("Invalid animal type")

# END

# Alternative solution

# class ConfigFactory:
#     def factory(file_path):
#         type = os.path.splitext(file_path)[1]
#         parser = PARSERS[type]()

#         raw_data = open(file_path).read()
#         data = parser.parse(raw_data)

#         return Config(data)

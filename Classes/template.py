from dataclasses import dataclass


@dataclass
class Klass:
    pass


def to_Klass(data):
    for key in data:
        setattr(Klass, key, data[key])

    object_ = Klass()
    return object_


data = {
    'key': 'value',
    'key2': 'value2',
}
config = to_Klass(data)

print(config.key)  # # value
print(config.key2)  # # value2

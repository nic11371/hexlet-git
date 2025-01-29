import json


# BEGIN (write your solution here)
class EqualityMixin:
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False


class SerializeMixin:

    def serialize(self):
        return json.dumps(self.__dict__['items'])

    @classmethod
    def deserialize(cls, data):
        return cls(json.loads(data))
# END

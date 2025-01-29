import json


# BEGIN
class EqualityMixin():
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False


class SerializeMixin():
    def serialize(self):
        return json.dumps(self.__dict__)

    @classmethod
    def deserialize(cls, data):
        attrs = json.loads(data)
        instance = cls(**attrs)
        return instance
# END

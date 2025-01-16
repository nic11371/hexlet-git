import copy


# BEGIN (write your solution here)
class InMemoryKV():
    def __init__(self, dictionary):
        self.dictionary = copy.deepcopy(dictionary)

    def set_(self, key, value):
        data = self.dictionary
        data[key] = value

    def unset_(self, key):
        data = self.dictionary
        result = data.pop(key)
        return result

    def get_(self, key, default=None):
        data = self.dictionary
        return data.get(key, default)

    def to_dict(self):
        data = self.dictionary
        return data
# END


def swap_key_value(obj):
    get_data = obj.to_dict()
    for k in get_data:
        obj.unset_(k)
    for k, v in get_data.items():
        obj.set_(v, k)


data = {'key': '10'}
mapping = InMemoryKV(data)
mapping.set_('key2', 'value2')
swap_key_value(mapping)
print(mapping.get_('key'))
print(mapping.get_(10))
print(mapping.get_('value2'))
# data['key2'] = 'value2'
# print(mapping.to_dict())
# print(data_copy)

def convert(tree):
    dictionary = {}

    def walk(node):
        key, child = node
        if isinstance(child, list):
            return key, convert(child)
        return key, child

    for item in tree:
        keys, value = walk(item)
        dictionary[keys] = value
    return dictionary


print(convert([]))
# {}
print(convert([('key2', 'value2'), ('key', 'value')]))
{'key2': 'value2', 'key': 'value'}
print(convert([
  ('key', [('key2', 'anotherValue')]),
  ('key2', 'value2')
]))
# {'key': {'key2': 'anotherValue'}, 'key2': 'value2'}

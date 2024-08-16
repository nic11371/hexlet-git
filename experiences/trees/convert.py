def convert(tree):
    dictionary = {}

    def walk(node):
        key, child = node
        dictionary[key] = child
        if isinstance(child, list):
            return key, convert(child)
        return key, child

    for item in tree:
        key, value = walk(item)
        dictionary[key] = value
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

def convert(tree):
    dictionary = {}

    def walk(node):
        for item in node:
            child = item[1]
            key = item[0]
            if isinstance(child, str):
                dictionary[key] = child
            else:
                return walk(child)
    walk(tree)
    return dictionary


# print(convert([]))
# # {}
# print(convert([('key2', 'value2'), ('key', 'value')]))
# {'key2': 'value2', 'key': 'value'}
print(convert([
  ('key', [('key2', 'anotherValue')]),
  ('key2', 'value2')
]))
# {'key': {'key2': 'anotherValue'}, 'key2': 'value2'}

# import itertools


def stringify(data, div=" ", count=1):
    if isinstance(data, str) or isinstance(data, int):
        return str(data)
    string = ''

    def walk(node, depth):
        key, value = node
        if isinstance(value, dict):
            return key, stringify(value)
        return key, str(value)

    _count = 0

    for items in data.items():
        key, value = walk(items, _count + 1)
        string += f"\n{key}: {value}"
    return string

# string = list(itertools.chain("{", ['hello'], ['world' + '\n' + "}"]))
# print('\n'.join(string))


print(stringify('hello'))
# # hello
# print(stringify(True))
# # True
# print(stringify(5))
# 5

data = {"hello": "world", "is": True, "nested": {"count": 5}}
print(stringify(data))  # то же самое что stringify(data, ' ', 1)
# {
#  hello: world
#  is: True
#  nested: {
#   count: 5
#  }
# }

# stringify(data, '|-', 2)
# # символ, переданный вторым аргументом повторяется столько раз,
# сколько указано третьим аргументом
# {
# |-|-hello: world
# |-|-is: True
# |-|-nested: {
# |-|-|-|-count: 5
# |-|-}
# }

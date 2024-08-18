import itertools


def stringify(data, div=" ", count=1, depth=0):
    if isinstance(data, str) or isinstance(data, int):
        return str(data)
    string = ''

    def walk(node):
        key, value = node
        if isinstance(value, dict):
            return key, stringify(value, depth + 1)
        return key, str(value)

    for items in data.items():
        key, value = walk(items)
        string += f"\n{key}: {value}"
        result = list(itertools.chain("{", string, "\n" + ' ', "}"))
    return ''.join(result)

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

import itertools


def stringify(value, space=" ", count=1):

    def iter_(data, depth):
        if not isinstance(data, dict):
            return str(data)

        deep_ident_size = count + depth
        deep_ident = space * deep_ident_size
        control = space * depth
        list = []
        for key, val in data.items():
            list.append(f"{deep_ident}{key}: {iter_(val, deep_ident_size)}")
        collection = itertools.chain('{', list, [control + '}'])
        return '\n'.join(collection)

    return iter_(value, 0)


print(stringify('hello'))
# hello
print(stringify(True))
# True
print(stringify(5))
5

data = {"hello": "world", "is": True, "nested": {"count": 5}}
print(stringify(data))  # то же самое что stringify(data, ' ', 1)
# {
#  hello: world
#  is: True
#  nested: {
#   count: 5
#  }
# }

print(stringify(data, '|-', 2))
# # символ, переданный вторым аргументом повторяется столько раз,
# сколько указано третьим аргументом
# {
# |-|-hello: world
# |-|-is: True
# |-|-nested: {
# |-|-|-|-count: 5
# |-|-}
# }

def get_unique(*args):
    result = set()
    for data in args:
        result |= set(data)
    return [*result]


print(get_unique([1, 2, 3], [3, 4, 5], [5, 6, 7]))

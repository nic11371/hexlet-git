def rotate_left(str):
    current = list(str)
    first = current.pop(0)
    current.append(first)
    return tuple(current)


def rotate_right(str):
    current = list(str)
    last = current.pop()
    current.insert(0, last)
    return tuple(current)


triple = ('A', 'B', 'C')
print(rotate_left(triple))  # ('B', 'C', 'A')
print(rotate_right(triple))  # ('C', 'A', 'B')
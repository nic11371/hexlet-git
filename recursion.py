def length(list_):
    if not list_:
        return 0
    return 1 + length(list_[1:])


def reverse_range(begin, end):
    if end == begin:
        return [end]
    return [end] + reverse_range(begin, end - 1)


def filter_positive(n):
    if not n:
        return n
    if n[0] <= 0:
        return filter_positive(n[1:])
    else:
        return [n[0]] + filter_positive(n[1:])


print(length([1, 2, 3]))  # 3
print(reverse_range(1, 1))  # [1]
print(reverse_range(1, 3))  # [3, 2, 1]
print(filter_positive([]))  # []
print(filter_positive([-3]))  # []
print(filter_positive([1, -2, 3]))  # [1, 3]

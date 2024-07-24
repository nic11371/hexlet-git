def length(n):
    if not n:
        return 0
    _, *tail = n
    return 1 + length(tail)


def reverse_range(begin, end):
    if begin == end:
        return [begin]
    return [end] + reverse_range(begin, end - 1)


def filter_positive(arr):
    if not arr:
        return []
    head, *tail = arr
    if head > 0:
        return [head] + filter_positive(tail)
    return filter_positive(tail)


print(length([1, 2, 3]))  # 3
print(reverse_range(1, 1))  # [1]
print(reverse_range(1, 3))  # [3, 2, 1]
print(filter_positive([]))  # []
print(filter_positive([-3]))  # []
print(filter_positive([1, -2, 3]))  # [1, 3]

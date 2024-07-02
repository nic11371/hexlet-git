from functools import reduce
from operator import truth, getitem


def keep_truthful(iterator):
    return filter(truth, iterator)


def abs_sum(numbers):
    arr = list(map(abs, numbers))
    return sum(arr)


def walk(dict, iterator):
    return reduce(getitem, iterator, dict)


print(list(keep_truthful([True, False, "", "foo"])))
print(abs_sum([-3, 7]))
print(abs_sum([]))
print(abs_sum([42]))
print(walk({'a': {7: {'b': 42}}}, ["a", 7, "b"]))
print(walk({'a': {7: {'b': 42}}}, ["a", 7]))

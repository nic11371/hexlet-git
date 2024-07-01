def filter_map(func, iterator):
    result = []
    filter = []
    for item in iterator:
        result.append(func(item))
    for elem in result:
        if elem[0]:
            filter.append(elem[1])
    return filter


def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''


for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
    print(s)

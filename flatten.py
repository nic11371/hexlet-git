def flatten(coll):
    if coll == []:
        return []
    new_flatten = []
    for item in coll:
        if isinstance(item, list):
            new_flatten = [*new_flatten, *item]
        else:
            new_flatten = [*new_flatten, item]
    return new_flatten


print(flatten([]))  # []
print(flatten([1, [3, 2], 9]))  # [1, 3, 2, 9]
print(flatten([1, [[2], [3]], [9]]))  # [1, [2], [3], 9]

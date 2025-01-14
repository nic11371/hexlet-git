def get_max(coll):
    if coll == []:
        return

    first, *rest = coll

    for item in rest:
        if first <= item:
            first = item

    return first


print(get_max([]))  # None
print(get_max([1, 10, 8]))  # 10
print(get_max([1, 2, 3, 4]))  # 4
print(get_max([-1, -2, -3]))  # -1

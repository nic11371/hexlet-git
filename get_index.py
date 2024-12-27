def get(coll, index, default_value=None):
    if index >= len(coll):
        return default_value
    if index < 0 and abs(index) > len(coll):
        return default_value
    return coll[index]


print(get(['moscow', 'proto', 'tula', '', None], -6, 'default'))

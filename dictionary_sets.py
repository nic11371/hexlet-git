def diff_keys(old, new):
    dictionary_result = {}
    dictionary_result['kept'] = new.keys() & old.keys()
    dictionary_result['added'] = new.keys() - old.keys()
    dictionary_result['removed'] = old.keys() - new.keys()
    return dictionary_result


print(diff_keys({'name': 'Bob', 'age': 42}, {}))
print(diff_keys({}, {'name': 'Bob', 'age': 42}))
print(diff_keys({'a': 2}, {'a': 1}))

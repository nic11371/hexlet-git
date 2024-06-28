def diff_keys(old_dictionary, new_dictionary):
    dictionary_result = {}
    dictionary_result['kept'] = new_dictionary.keys() & old_dictionary.keys()
    dictionary_result['added'] = new_dictionary.keys() - old_dictionary.keys()
    dictionary_result['removed'] = old_dictionary.keys() - new_dictionary.keys()
    return dictionary_result


print(diff_keys({'name': 'Bob', 'age': 42}, {}))
print(diff_keys({}, {'name': 'Bob', 'age': 42}))
print(diff_keys({'a': 2}, {'a': 1}))

import os
import sys
from algorithms_basics.hashes.hash.Hash import Hash

sys.path.append(os.path.abspath('/usr/src/app/'))


def remove(hash, key):
    removed = None
    index = hash.calculate_index(hash.table, key)
    record = hash.table[index].head
    if record is None:
        return None

    while record and record.value['key'] == key:
        removed = record.value['value']
        record = record.next
        hash.count = - 1
    # current_node = record

    while record.next is not None:
        if record.next.value['key'] == key:
            removed = record.next.value['value']
            record.next = record.next.next
            hash.count =- 1
        else:
            record = record.next

    if hash.table[index].tail.value['key'] is not None:
        hash.table[index].tail = record

    return removed


# def solution(map, key):
#     hash = Hash()
#
#     for key_, value in map.items():
#         hash.set(key_, value)
#
#     return remove(hash, key)


table = Hash()
table.set("key", "value")
table.set("key1", "value1")
print(remove(table, 'key'))

# removed = solution(table, "key")
# print(removed)  # => value

# В хеше ключа больше нет
print(table.get("key"))  # None

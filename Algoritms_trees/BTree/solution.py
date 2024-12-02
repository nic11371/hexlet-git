import os
import sys
from helpers import buildBTree
from fixtures.tree2 import dictionary as data

sys.path.append(os.path.abspath('/usr/src/app/'))


# BEGIN (write your solution here)
def find_values_in_range(root, min, max, found_range=None):
    if found_range is None:
        found_range = []
    for i in range(len(root.keys)):
        if root.keys[i] >= min and root.keys[i] <= max:
            found_range.append(root.keys[i])
    for node in root.children:
        find_values_in_range(node, min, max, found_range)
    return found_range


def solution(items, min, max):
    btree = buildBTree(items)
    return find_values_in_range(btree, min, max)


print(solution(data, 30, 50))

# END

# def find_values_in_range(node, min, max):
#     values = []
#     keys = node.keys
#     children = node.children

#     # Поиск значений в текущем узле
#     for i in range(len(keys)):
#         if keys[i] >= min and keys[i] <= max:
#             values.append(keys[i])

#     # Рекурсивный поиск значений в дочерних узлах
#     if not node.leaf:
#         for i in range(len(children)):
#             if i == 0 and keys[0] >= min:
#                 values.extend(find_values_in_range(children[i], min, max))
#             elif i == len(children) - 1 and keys[-1] <= max:
#                 values.extend(find_values_in_range(children[i], min, max))
#             elif i < len(children) - 1 and (keys[i] >= min and keys[i] <= max):
#                 values.extend(find_values_in_range(children[i], min, max))

#     return values

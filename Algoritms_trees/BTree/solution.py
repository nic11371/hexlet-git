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

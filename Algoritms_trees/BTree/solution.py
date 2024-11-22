import os
import sys
from helpers import buildBTree
from fixtures.tree2 import dictionary as data

sys.path.append(os.path.abspath('/usr/src/app/'))


# BEGIN (write your solution here)
def find_values_in_range(root, value, min, max):
    while root:
        for i in range(len(root.keys)


def solution(items, min, max):
    btree = buildBTree(items)
    return find_values_in_range(btree, min, max)


print(solution(data, 30, 50))

# END

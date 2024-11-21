import os
import sys
from helpers import build_RBTree
from fixtures.tree2 import dictionary as data2
from fixtures.tree import dictionary as data1

sys.path.append(os.path.abspath('/usr/src/app/'))


# BEGIN (write your solution here)
def count_black_nodes(node, count=0):
    if node:
        if node.is_red is False:
            count += 1
            count += count_black_nodes(node.left)
    return count


def solution(arr):
    tree = build_RBTree(arr)
    return count_black_nodes(tree)


print(solution(data1))
print(solution(data2))

# END

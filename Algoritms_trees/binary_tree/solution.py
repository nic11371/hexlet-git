import os
import sys
from helpers import sorted_array_to_BST

sys.path.append(os.path.abspath('/usr/src/app/'))


# BEGIN (write your solution here)
def traverse(node, path=None, paths=None):
    if node:
        if path is None:
            path = []
        if paths is None:
            paths = []
        path.append(node.value)
        traverse(node.left, path, paths)
        traverse(node.right, path, paths)
        if node.left is None and node.right is None:
            paths.append(list(path))
        return paths


def solution(arr):
    if arr == []:
        return []
    tree = sorted_array_to_BST(arr)
    current_node = traverse(tree)
    return current_node


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# END

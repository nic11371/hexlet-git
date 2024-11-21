import os
import sys

sys.path.append(os.path.abspath('/usr/src/app/'))

from helpers import sorted_array_to_BST


# BEGIN (write your solution here)
def traverse(node):
    if node is not None:
        print(f"node = {node.value}")
        traverse(node.left)
        traverse(node.right)
        return node.value


def solution(arr):
    current_path = []
    paths = []
    tree = sorted_array_to_BST(arr)
    current_node = traverse(tree)
    if current_node:
        current_path.append(current_node)
        traverse(tree)
    
    paths.append(current_node) 
    return paths

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# END

import os
import sys
# from fixtures.tree2 import dictionary as data
from helpers import ASTree


sys.path.append(os.path.abspath('/usr/src/app/'))


# BEGIN (write your solution here)
def find_values_in_range(root, min, max, found_range=None):
    if found_range is None:
        found_range = []
    return found_range


def solution(items):
    btree = ASTree.buildAST(items)
    return btree


structure = ['assign', ['a', ['sum', [['multiply', [5, 10]], ['sqrt', 6]]]]]
ast = ASTree.buildAST(structure)
print(solution(ast))
# => ['assign',['a',['sum',[['multiply',[5,10]],['sqrt',6]]]]]
# print(solution(data, 30, 50))

# END

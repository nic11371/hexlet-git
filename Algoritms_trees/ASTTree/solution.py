import os
import sys
from fixtures.tree2 import tree as data
from helpers import ASTree


sys.path.append(os.path.abspath('/usr/src/app/'))


# BEGIN (write your solution here)
def find_values_in_range(root, min, max, found_range=None):
    if found_range is None:
        found_range = []
    return found_range


def solution(items):
    result = []
    result.append(items['operator'])
    if items['instructionType'] == 'unary':
        result.append(solution(items['children']))
    if items['instructionType'] == 'multiple':
        intermediate = [solution(elem) for elem in items['children']]
        result.append(intermediate)
    if items['instructionType'] == 'argument':
        return items['value']

    return result


structure = ['assign', ['a', ['sum', [['multiply', [5, 10]], ['sqrt', 6]]]]]
ast = ASTree.buildAST(structure)
print(solution(data))
# => ['assign',['a',['sum',[['multiply',[5,10]],['sqrt',6]]]]]
# print(solution(data, 30, 50))

# END

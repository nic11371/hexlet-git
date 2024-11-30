import os
import sys
from helpers import buildBTree
from fixtures.tree2 import dictionary as data

sys.path.append(os.path.abspath('/usr/src/app/'))


# BEGIN (write your solution here)
def find_values_in_range(root, min, max):
    found_range = []
    def walk(root):
        while root:
            for i in range(len(root.keys)):
                if root.keys[i] >= min and root.keys[i] <= max:
                    found_range.append(root.keys[i])
                if min < root.keys[i]:
                    if not root.leaf:
                        if i < len(root.children):
                            root = root.children[i]
                        else:
                            return None
                        break
                    else:
                        continue
                elif i == len(root.keys) - 1 and not root.leaf:
                    if i + 1 < len(root.children):
                        root = root.children[i + 1]
                    else:
                        return None
                    break
            else:
                break
        return None
    walk(root)
    return found_range       

def solution(items, min, max):
    btree = buildBTree(items)
    return find_values_in_range(btree, min, max)


print(solution(data, 40, 70))

# END

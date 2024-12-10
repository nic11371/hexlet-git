# import os
# import sys
# from helpers import build_tree
# from fixtures.tree2 import words as data

# sys.path.append(os.path.abspath('/usr/src/app/'))


# # BEGIN (write your solution here)
# def find_points_in_radius(node, point, radius):
#     points, depth, dimensions, parent = node
#     bestChild = None
#     dimension = dimensions[node.dimension]
#     ownDistance = metric(point, node.point)
#     linearPoint = {}
#     linearDistance = 0
#     otherChild = None
    


# def solution(points, center_point, radius):
#     tree = build_tree(points, 0, ['x', 'y'], None)
#     return find_points_in_radius(tree, center_point, radius)


# print(solution(data, {'x': 4, 'y': 5}, 2))

# # // [
# # //    { x:3, y:4 },
# # //    { x:5, y:6 }
# # // ]
# # END

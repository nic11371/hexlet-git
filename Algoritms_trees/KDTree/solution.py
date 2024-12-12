from helpers import build_tree
from fixtures.tree1 import points as data1
from fixtures.tree2 import points as data2


# BEGIN (write your solution here)

def find_points_in_radius(node, center_point, radius):
    if node is None:
        return []

    dx = center_point['x'] - node.point['x']
    dy = center_point['y'] - node.point['y']

    distance_square = dx * dx + dy * dy

    if distance_square <= radius * radius:
        return [node.point] + \
            find_points_in_radius(node.left, center_point, radius) + \
            find_points_in_radius(node.right, center_point, radius)

    if node.dimension == 'x' and node.point['x'] - radius <= node.point['x']:
        return find_points_in_radius(node.left, center_point, radius) + \
                find_points_in_radius(node.right, center_point, radius)

    if node.dimension == 'y' and node.point['y'] - radius <= node.point['y']:
        return find_points_in_radius(node.left, center_point, radius) + \
                find_points_in_radius(node.right, center_point, radius)

    return find_points_in_radius(node.right, center_point, radius)


def solution(points, center_point, radius):
    tree = build_tree(points, 0, ['x', 'y'], None)
    return find_points_in_radius(tree, center_point, radius)


print(solution(data1, {'x': -2, 'y': 2}, 3))
print(solution(data2, {'x': 4, 'y': 5}, 2))

# END

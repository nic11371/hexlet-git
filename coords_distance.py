def calculate_distance(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


point1 = [0, 0]
point2 = [3, 4]
print(calculate_distance(point1, point2))

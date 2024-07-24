def get_mid_point(point_1, point_2):
    x1 = point_1['x']
    x2 = point_2['x']
    y1 = point_1['y']
    y2 = point_2['y']
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return {'x': x, 'y': y}


point1 = {'x': 0, 'y': 0}
point2 = {'x': 4, 'y': 4}
print(get_mid_point(point1, point2))

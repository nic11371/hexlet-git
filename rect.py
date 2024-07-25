def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None


def make_rectangle(point, width, height):
    return {'point': point, 'width': width, 'height': height}


def get_start_point(point):
    return point['point']


def get_width(point):
    return point['width']


def get_height(point):
    return point['height']


def contains_origin(rect):
    point_1 = get_start_point(rect)
    point_2 = make_decart_point(
            get_x(point_1) + get_width(rect),
            get_y(point_1) - get_height(rect))
    quad_1 = get_quadrant(point_1)
    quad_2 = get_quadrant(point_2)
    # return quad_1 == 2 and quad_2 == 4
    if quad_1 != quad_2:
        if quad_1 is None or quad_2 is None:
            return False
        return True
    return False


p = make_decart_point(0, 1)
rectangle = make_rectangle(p, 4, 5)
print(rectangle)
print(get_start_point(rectangle))
print(get_width(rectangle))
print(get_height(rectangle))
print(contains_origin(rectangle))  # False

rectangle2 = make_rectangle(make_decart_point(-4, 3), 5, 4)
print(contains_origin(rectangle2))  # True

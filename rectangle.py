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
    return point, width, height


def get_start_point(point):
    return point[0]


def get_width(point):
    return point[1]


def get_height(point):
    return point[2]


def contains_origin(rect):
    point_1 = get_start_point(rect)
    point_2 = get_x(point_1) + get_width(rect)
    point_3 = get_x(point_1) + get_width(rect) + get_height(rect)
    point_4 = get_y(point_1) + get_height(rect)
    quad_1 = get_quadrant(point_1)
    quad_2 = get_quadrant(point_2)
    quad_3 = get_quadrant(point_3)
    quad_4 = get_quadrant(point_4)
    if quad_1 != quad_2 != quad_3 != quad_4:
        return True
    return False


p = make_decart_point(0, 1)
rectangle = make_rectangle(p, 4, 5)
print(rectangle)
print(get_start_point(rectangle))
print(contains_origin(rectangle))  # False

rectangle2 = make_rectangle(make_decart_point(-4, 3), 5, 4)
print(contains_origin(rectangle2))  # True

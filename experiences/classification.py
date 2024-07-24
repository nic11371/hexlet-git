def is_degenerated(coords):
    (x1, y1), (x2, y2) = coords
    if x1 == x2 and y1 == y2:
        return True
    return False


def is_vertical(coords):
    (x1, y1), (x2, y2) = coords
    if x1 == x2 and y1 == y2:
        return False
    if x1 == x2:
        return True
    return False


def is_horizontal(coords):
    (x1, y1), (x2, y2) = coords
    if x1 == x2 and y1 == y2:
        return False
    if y1 == y2:
        return True
    return False


def is_inclined(coords):
    (x1, y1), (x2, y2) = coords
    if x1 != x2 and y1 != y2:
        return True
    return False


line_1 = (0, 10), (100, 130)
print(is_vertical(line_1))  # False
print(is_horizontal(line_1))  # False
print(is_degenerated(line_1))  # False
print(is_inclined(line_1))  # True
line_2 = (42, 1), (42, 2)
print(is_vertical(((15, 5), (15, -5))))  # True
print(is_vertical(((5, 15), (-5, 15))))  # True
print(is_vertical(((42, 100), (42, 100))))  # False
line_3 = (100, 50), (200, 50)
print(is_horizontal(line_3))  # True

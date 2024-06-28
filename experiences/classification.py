def is_degenerated(coords):
    if coords[0][0] == coords[1][0] and coords[1][0] == coords[1][1]:
        return True
    return False


def is_vertical(coords):
    if coords[0][0] == coords[1][0]:
        return True
    return False


def is_horizontal(coords):
    if coords[0][1] == coords[1][1]:
        return True
    return False


def is_inclined(coords):
    if coords[0][0] != coords[1][0] and coords[1][0] != coords[1][1]:
        return True
    return False



line1 = (0, 10), (100, 130)
print(is_vertical(line1))  # False
print(is_horizontal(line1))  # False
print(is_degenerated(line1))  # False
print(is_inclined(line1))  # True
line2 = (42, 1), (42, 2)
print(is_vertical(line2))  # True
line3 = (100, 50), (200, 50)
print(is_horizontal(line3))  # True
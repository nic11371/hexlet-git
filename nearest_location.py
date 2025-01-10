import math


def get_distance(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    xs = x2 - x1
    ys = y2 - y1

    return math.sqrt(xs ** 2 + ys ** 2)


# BEGIN (write your solution here)
def get_the_nearest_location(locations, point):
    if locations == []:
        return None

    nearest_location = locations[0]
    _, local_point = nearest_location
    min_distance = get_distance(point, local_point)

    for location in locations:
        _, local_point = location
        current_distance = get_distance(point, local_point)
        if current_distance <= min_distance:
            min_distance = current_distance
            nearest_location = location

    return nearest_location


locations = [
  ['Park', [10, 5]],
  ['Sea', [1, 3]],
  ['Museum', [8, 4]],
]

locations2 = [
    ['Hotel', [7, 3]],
    ['Square', [5, 6]],
]

locations3 = [
    ['Hotel', [1, 2]],
    ['Square', [5, 6]],
]

print(get_the_nearest_location(locations, [5, 5]))
print(get_the_nearest_location(locations, [1, 3]))
print(get_the_nearest_location(locations2, [1, 3]))
print(get_the_nearest_location(locations3, [1, 3]))
# END

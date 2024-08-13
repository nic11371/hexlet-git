def diff(degrees_1, degrees_2):
    minimum = abs(min(degrees_1, degrees_2)) % 360
    maximum = abs(max(degrees_1, degrees_2)) % 360
    result = maximum - minimum
    if 0 >= result <= 180:
        return result
    return 360 - maximum + minimum


print(diff(-60, 60))
# 45
print(diff(-100, 200))
# 180
print(diff(0, 190))  # не 190, а 170, потому что 170 меньше
# 170
print(diff(120, 280))
# 160

def diff(degrees_1, degrees_2):
    different = degrees_1 - degrees_2
    result = 0
    result = different % 360
    if result > 180:
        return 360 - result
    return result


# def diff(angle1, angle2):
#     return min(
#         (angle1 - angle2) % 360,
#         (angle2 - angle1) % 360,
#     )


print(diff(0, 45))  # 45
print(diff(0, 180))  # 180
print(diff(0, 190))  # не 190, а 170, потому что 170 меньше # 170
print(diff(120, 280))  # 160
print(diff(315, 45))  # 270
print(diff(45, 135))  # 90
print(diff(240, 30))  # 210

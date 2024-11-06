def solution(array):
    e = 0
    i = 0
    while e < len(array):
        if array[e] % 2 == 1:
            array[e], array[i] = array[i], array[e]
            i += 1
        e += 1
    return array


arr = [3, 1, 12, 7, 8, 1, 6, 4]
print(solution(arr))  # [3, 1, 7, 1, 8, 12, 6, 4]

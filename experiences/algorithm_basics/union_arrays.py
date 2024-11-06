def solution(arr1, arr2):
    union = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            union.append(arr1[i])
            i += 1
        else:
            union.append(arr2[j])
            j += 1

    while i < len(arr1):
        union.append(arr1[i])
        i += 1

    while j < len(arr2):
        union.append(arr2[j])
        j += 1

    return union

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 8, 12]

print(solution(arr1, arr2))

def solution(item):
    left = 0
    right = len(item) - 1
    length = right - left + 1

    while True:
        pivot = item[left]
        if length < 2:
            return
        
        while items[right] > pivot:
            right -= 1
        while items[left] < pivot:
            left += 1
        if left >= right:
            return right + 1
        item[left], item[right] = item[right], item[left]
        left += 1
        right -= 1
        split_index = partition(items, left, right, pivot)
        sort(items, left, split_index - 1)
        sort(items, split_index, right)





items = [10, 20, 0, -1]

print(solution(items))  # [-1, 0, 10, 20]
# print(solution([]))  # []
# print(solution(items, 'desc'))  # [20, 10, 0, -1]

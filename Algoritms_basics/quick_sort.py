def solution(items, dir='asc'):
    if len(items) < 2:
        return items
    else:
        pivot = items[len(items) // 2]
        left = [i for i in items[1:] if i <= pivot]
        right = [i for i in items[1:] if i > pivot]
        if dir == 'desk':
            return solution(right, dir) + [pivot] + solution(left, dir)
        return solution(right) + [pivot] + solution(left)


items = [10, 3, 20, 1, 0, -1, 20, 3, 1, 3]

print(solution(items, 'desk'))  # [-1, 0, 10, 20]
print(solution([]))  # []
print(solution(items, 'desc'))  # [20, 10, 0, -1]

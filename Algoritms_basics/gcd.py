def solution(a, b):
    if a == b:
        return a
    if a > b:
        return solution(a - b, b)
    else:
        return solution(a, b - a)


print(solution(38, 28))  # => 2
print(solution(129, 90))  # => 3
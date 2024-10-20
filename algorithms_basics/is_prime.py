def solution(n):
    if n <= 1:
        return False
    k = 0
    for i in range(2, int(n // 2) + 1):
        if n % i == 0:
            k += 1
        return True if k <= 0 else False


print(solution(2147483648))  # False
print(solution(87178291199))  # True

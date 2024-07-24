def is_perfect(n):
    if n == 0:
        return False
    limit = n // 2 + 1
    sum = 0
    for i in range(1, limit):
        if n % i == 0:
            sum += i
    if n == sum:
        return True
    return False


print(is_perfect(6))  # True
print(is_perfect(1))  # False

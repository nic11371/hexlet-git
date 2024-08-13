def is_power_of_three(n):
    if n < 1:
        return False
    while (n % 3 == 0):
        n /= 3
    return n == 1


print(is_power_of_three(1))  # True
print(is_power_of_three(2))  # False
print(is_power_of_three(9))  # True

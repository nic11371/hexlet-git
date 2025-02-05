def smallest_divisor(n):
    if n == 1:
        return 1

    def inner(count, acc):
        if count == 1:
            return acc
        if n % count == 0:
            acc = count
        return inner(count - 1, acc)

    return inner(n, 1)


# def smallest_divisor(num):
#     def iter(acc):
#         # Мы используем 'num // 2' в условии, а не 'num'.
#         # Эта простая оптимизация позволит нам скоратить число проверок
#         if acc > num // 2:
#             return num
#         if num % acc == 0:
#             return acc
#         return iter(acc + 1)

#     # Особый случай для числа 1
#     if num == 1:
#         return 1

#     return iter(2)


print(smallest_divisor(1))
print(smallest_divisor(3))
print(smallest_divisor(4))
print(smallest_divisor(8))
print(smallest_divisor(9))
print(smallest_divisor(17))
print(smallest_divisor(15))
print(smallest_divisor(121))

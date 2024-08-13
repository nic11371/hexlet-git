def sum_of_square_digits(num):
    integer_square = 0
    for i in str(num):
        prev = int(i) ** 2
        integer_square += prev
    return integer_square


def is_happy_number(num):
    value_number = sum_of_square_digits(num)
    count = 1
    while count <= 10:
        value_number = sum_of_square_digits(str(value_number))
        count += 1
    if value_number == 1:
        return True
    return False


# print(sum_of_square_digits(23))
print(is_happy_number(13))

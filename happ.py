def sum_of_square_digits(num):
    integer_square = 0
    for i in str(num):
        count = int(i) ** 2
        integer_square += count
    return integer_square

# def is_happy_number(num):
#   pass




print(sum_of_square_digits(23))
# print(is_happy_number(7))
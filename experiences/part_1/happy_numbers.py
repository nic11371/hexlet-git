def sum_of_square_digits(num): 
    integer_square = 1
    for i in str(num):
        integer_square = integer_square * int(i)


def is_happy_number(num):
    pass


print(sum_of_square_digits(7))
print(is_happy_number(7))

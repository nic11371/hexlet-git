def fizz_buzz(begin, end):
    string = []
    if begin > end:
        return ''
    for i in range(begin, end + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            string.append("FizzBuzz")
        elif i % 3 == 0:
            string.append("Fizz")
        elif i % 5 == 0:
            string.append("Buzz")
        else:
            string.append(str(i))
    return " ".join(string)


print(fizz_buzz(1, 5))
# => 1 2 Fizz 4 Buzz
print(fizz_buzz(11, 20))
# => 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz

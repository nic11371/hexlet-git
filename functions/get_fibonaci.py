def get_fibonacci():
    i = 0
    a, b = 1, 0
    while True:
        a, b = b, a + b
        yield a
        i += 1


fib = get_fibonacci()
for x in fib:
    print(x)
    if x > 5:
        break

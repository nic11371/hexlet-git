def cons(a, b):
    def f(message):
        if message == "car":
            return a
        if message == "cdr":
            return b
    return f


def car(pair):
    return pair("car")


pair = cons(4, 5)
print(car(pair))

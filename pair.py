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


def cons_1(head, tail):
    return lambda selector: selector(head, tail)


# BEGIN (write your solution here)
def car_1(pair):
    return pair(lambda head, tail: head)


def cdr_1(pair):
    return pair(lambda head, tail: tail)


pair_1 = cons(5, 3)
print(car_1(pair_1))
print(cdr_1(pair_1))

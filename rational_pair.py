def make(numer, denom):
    return {'numer': numer, 'denom': denom}


def numer(pair):
    return pair['numer']


def denom(pair):
    return pair['denom']


def to_string(pair):
    return f"{numer(pair)} / {denom(pair)}"


def is_equal(rat_1, rat_2):
    if numer(rat_1) * denom(rat_2) == numer(rat_2) * denom(rat_1):
        return True
    return False


def add(rat_1, rat_2):
    a = numer(rat_1)
    b = denom(rat_1)
    c = numer(rat_2)
    d = denom(rat_2)
    return {
        'numer': a * d + b * c,
        'denom': b * d
    }


def sub(rat_1, rat_2):
    a = numer(rat_1)
    b = denom(rat_1)
    c = numer(rat_2)
    d = denom(rat_2)
    return {
        'numer': a * d - b * c,
        'denom': b * d
    }


def mul(rat_1, rat_2):
    a = numer(rat_1)
    b = denom(rat_1)
    c = numer(rat_2)
    d = denom(rat_2)
    return {
        'numer': a * c,
        'denom': b * d
    }


def div(rat_1, rat_2):
    a = numer(rat_1)
    b = denom(rat_1)
    c = numer(rat_2)
    d = denom(rat_2)
    return {
        'numer': a * d,
        'denom': b * c
    }


rat1 = make(2, 3)
rat12 = make(4, 6)
rat2 = make(7, 2)
print(to_string(rat12))  # '4 / 6'
print(is_equal(rat1, rat12))  # True
print(add(rat1, rat2))  # 25/6
print(sub(rat2, rat1))  # 17/6
print(mul(rat1, rat2))  # 14/6
print(div(rat1, rat2))  # 4/21

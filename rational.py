import math


def make(numer, denom):
    normalize = math.gcd(numer, denom)
    return {'numer': int(numer / normalize), 'denom': int(denom / normalize)}


def get_numer(rat):
    return rat['numer']


def get_denom(rat):
    return rat['denom']


def add(r1, r2):
    return make(
        get_numer(r1) * get_denom(r2) + get_denom(r1) * get_numer(r2),
        get_denom(r1) * get_denom(r2)
    )


def sub(r1, r2):
    return make(
        get_numer(r1) * get_denom(r2) - get_denom(r1) * get_numer(r2),
        get_denom(r1) * get_denom(r2)
    )


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"


rat1 = make(3, 9)
get_numer(rat1)  # 1
get_denom(rat1)  # 3
rat2 = make(10, 3)
rat3 = add(rat1, rat2)
print(to_str(rat3))  # 11/3
rat4 = sub(rat1, rat2)
print(to_str(rat4))  # -3/1

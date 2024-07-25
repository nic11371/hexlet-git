import math


def make(numer, denominator):
    return {'numer': numer, 'denominator': denominator}


def get_numer(rat):
    return rat['numer']


def get_denom(rat):
    return rat['denominator']


def add(rat_1, rat_2):
    gcd_ = math.gcd(get_denom(rat_1), get_denom(rat_2))
    return gcd_


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"


rat1 = make(3, 9)
get_numer(rat1)  # 1
get_denom(rat1)  # 3
rat2 = make(10, 3)
rat3 = add(rat1, rat2)
print(rat3)
# to_str(rat3)  # 11/3
# rat4 = sub(rat1, rat2)
# to_str(rat4)  # -3/1

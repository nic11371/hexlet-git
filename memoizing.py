from functools import wraps
from collections import OrderedDict


def memoizing(max_remember):

    def memoized(func):
        cache = OrderedDict({})

        @wraps(func)
        def wrapper(number):
            if number in cache.keys():
                return cache.get(number)
            calculation = func(number)
            cache[number] = calculation
            if len(cache) > max_remember:
                cache.popitem(last=False)
            return calculation
        return wrapper
    return memoized


@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
# => Calculating...
# 10
print(f(1))  # будет "вспомнено"
# 10
print(f(2))
# => Calculating...
# 20
print(f(3))
# => Calculating...
# 30
print(f(4))  # вытеснит запомненный результат для "1"
# => Calculating...
# 40
print(f(1))  # будет перевычислено
# => Calculating...
# 10

def memoizing(limit):
    def wrapper(function):
        memory = {}
        order = []

        def inner(argument):
            memoized_result = memory.get(argument)
            if memoized_result is None:
                memoized_result = function(argument)
                memory[argument] = memoized_result
                order.append(argument)
                if len(order) > limit:
                    oldest_argument = order.pop(0)
                    memory.pop(oldest_argument)
            return memoized_result
        return inner
    return wrapper


@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10


f(1)
# => Calculating...
# 10
f(1)  # будет "вспомнено"
# 10
f(2)
# => Calculating...
# 20
f(3)
# => Calculating...
# 30
f(4)  # вытеснит запомненный результат для "1"
# => Calculating...
# 40
f(1)  # будет перевычислено
# => Calculating...
# 10

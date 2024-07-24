def partial_apply(func, name):
    def inner(surname):
        return func(name, surname)
    return inner


def greet(name, surname):
    return f'Hello, {name} {surname}!'


f = partial_apply(greet, 'Dorian')
print(f('Grey'))


def flip(func):
    def inner(name, surname):
        return func(surname, name)
    return inner


def greet_flip(name, surname):
    return f'Hello, {name} {surname}!'


f = flip(greet_flip)
print(f('Christian', 'Teodor'))

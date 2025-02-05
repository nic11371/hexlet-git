def partial_apply(fn, name):
    def walk(surname):
        return fn(name, surname)
    return walk


def flip(fn):
    def walk_flip(name, surname):
        return fn(surname, name)
    return walk_flip
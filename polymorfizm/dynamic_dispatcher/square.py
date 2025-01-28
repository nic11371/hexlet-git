from polymorfizm.dynamic_dispatcher import defmethod


# BEGIN (write your solution here)
def init():
    defmethod(__name__, 'get_area', lambda self: self['data']['side'] ** 2)


def make(side):
    return {'name': __name__, 'data': {'side': side}}


def get_side(self):
    return self['data']['side']

# END

from polymorfizm.dynamic_dispatcher import defmethod
from math import pi


def init():
    defmethod(__name__, 'get_area', lambda self: pi * self['data']['radius'] ** 2)


def make(radius):
    return {'name': __name__, 'data': {'radius': radius}}


def get_circle_radius(self):
    return self['data']['radius']


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coord: " + str(self.__dict__)


def wrapper(func):
    def checker(*args):
        for a in args:
            if a.x < 0 or a.y < 0:
                a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)

        ret = func(*args)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else ret.y)
        return ret
    return checker

@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

@wrapper
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

add = wrapper(add)
sub = wrapper(sub)
one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)

print(add(one, two))
print(sub(one, two))
print(add(one, three))
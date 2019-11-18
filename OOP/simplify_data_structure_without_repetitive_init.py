import math


class Structure:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        # set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # set the remaining keywords arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError("Invalid arguments(s): {}".format(",".join(kwargs)))


if __name__ == "__main__":
    class Stock(Structure):
        _fields = ["name", "share", "price"]

    class Point(Structure):
        _fields = ["x", "y"]

    class Circle(Structure):
        _fields = ["radius"]

        def area(self):
            return math.pi * self.radius ** 2

    s = Stock("ACME", 50, 91.1)
    p = Point(2, 3)
    c = Circle(4.5)

    print(s.name)
    print(p.x)
    print(c.radius)


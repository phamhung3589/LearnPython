class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

        def __set__(self, instance, value):
            instance.__dict__[self.name] = value


# class decorator to apply constraints
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate


# @check_attributes(name=SizeString(size=9),
#                   shares=UnsignedInteger,
#                   price=UnsignedFloat)
# class Stock:
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
#
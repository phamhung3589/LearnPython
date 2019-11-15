class Logger(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_logger"):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)

        return cls._logger


obj1 = Logger()
obj2 = Logger()

print(obj1 == obj2)
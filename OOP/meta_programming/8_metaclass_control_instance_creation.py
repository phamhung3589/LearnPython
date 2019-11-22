class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


# Example
class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print("spam.grok")


# Create singleton design pattern
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class test_singleton(metaclass=Singleton):
    def __init__(self):
        print("Creating Spam")


if __name__ == "__main__":
    print(Spam.grok(10))

    a = test_singleton()
    b = test_singleton()
    c = test_singleton()

    print(a is b and b is c and c is a)

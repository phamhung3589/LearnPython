from functools import wraps


class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("decorator 1")
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("decorator 2")
            return func(*args, **kwargs)
        return wrapper


if __name__ == "__main__":
    a = A()

    @a.decorator1
    def spam():
        pass

    @A.decorator2
    def grok():
        pass

    spam()
    grok()

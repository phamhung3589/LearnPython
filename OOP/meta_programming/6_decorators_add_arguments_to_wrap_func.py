from functools import wraps
import inspect


def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


@optional_debug
def spam2(a, b):
    print(a, b)


if __name__ == "__main__":
    spam(3, 5, 6, debug=True)
    spam2(9, 10)
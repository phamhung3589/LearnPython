from functools import wraps, partial
import logging


# Utility decorator to attach a function as an attribute of abj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    '''
    Add logging to a function.
    :param level:   logging level
    :param name:    logger name
    :param message: log message
    :return: if name and message aren't specified, the default to the function's module and name
    '''

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_msg):
            nonlocal logmsg
            logmsg = new_msg

        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x+y


@logged(logging.CRITICAL, "example")
def spam():
    print("Spam!")


if __name__ == "__main__":
    a = add(2, 3)
    print(add.set_message("Add called"))
    spam()

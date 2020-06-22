from functools import wraps

from datetime import datetime

# Name of log file
filename = 'logged-classes.log'


# Base class for logging all calls of methods
class Logger:

    def _decorator(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_now = datetime.now().time().strftime('%H:%M:%S')
            class_name = type(self).__name__
            func_name = func.__name__
            string = f"{time_now}: {class_name}, {func_name}, {args, kwargs}\n"

            with open(filename, "a+") as file:
                file.write(string)

            return func(*args, **kwargs)

        return wrapper

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if callable(value):
            decorator = object.__getattribute__(self, '_decorator')
            return decorator(value)
        return value


class Child(Logger):

    def test(self, a):
        print(f"Test 1 = {a}")


class Child2(Logger):

    def test2(self, b):
        print(f"Test 2 = {b}")


class GrandChild(Child):

    def test3(self, c):
        print(f"Test 3 = {c}")


if __name__ == "__main__":

    # Tests

    # Creattion instances of Classes
    a = Child()
    b = Child2()
    c = GrandChild()

    # Calls of methods of Classes
    a.test(5)
    b.test2(6)
    c.test3(7)
    c.test(8)

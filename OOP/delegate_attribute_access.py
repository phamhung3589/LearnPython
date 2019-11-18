class A:
    def spam(self, x):
        print("A.spam", x)

    def foo(self):
        print("A.foo")


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print("B.spam", x)
        self._a.spam(x)

    def bar(self):
        print("B.bar")

    def __getattr__(self, name):
        return getattr(self._a, name)


if __name__ == "__main__":
    a = A()
    a.spam(2)
    a.foo()

    b = B()
    b.spam(3)
    print(b.foo())
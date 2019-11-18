class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expect a string")
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def first_name(self):
        print("getiting name")
        return super().first_name

    @first_name.setter
    def first_name(self, value):
        print("setting name to ", value)
        super(SubPerson, SubPerson).first_name.__set__(self, value)

    @first_name.deleter
    def first_name(self):
        print("deleting name")
        super(SubPerson, SubPerson).first_name.__delete__(self)


p = SubPerson("hung")
p.first_name = "Huy"
# print(p.first_name)

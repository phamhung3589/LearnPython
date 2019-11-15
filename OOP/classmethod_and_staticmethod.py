# python program to demonstrate use of class method and staticmethod
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # A lcass method to create a Person object by birth year -
    # using replace for overloading in java (same method, difference parameter) - polymorphism
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def is_adult(age):
        return age > 18


if __name__ == "__main__":
    person1 = Person("hung", 24)
    person2 = Person.from_birth_year("hung", 1995)

    print(person1.age)
    print(person2.age)

    # print the result
    print(Person.is_adult(24))
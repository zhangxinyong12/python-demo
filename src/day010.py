# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#
# p = Person('wang', 20)
# print(p.age)
# # p157


class Book:
    def __str__(self):
        return '11111'


class Computer:
    pass


class Student:
    pass


book = Book()
print(book)
# p 160
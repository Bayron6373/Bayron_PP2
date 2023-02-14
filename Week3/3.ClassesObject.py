#Try it yourself
#To create a class, use the keyword class:
class Myclass:
    x = 5
print(Myclass)

class Myclass2:
    x = 5
p1 = Myclass2()
print(p1.x)
#To understand the meaning of classes we have to understand the built-in __init__() function.
#All classes have a function called __init__(), which is always executed when the class is being initiated.
class Person:
    def _init_(self,name,age):
        self.name = name
        self.age = age

p2 = Person("Bayron",18)
print(p2.name)
print(p2.age)
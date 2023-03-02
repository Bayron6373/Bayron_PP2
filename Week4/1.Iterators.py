#Try it yourself
mytuple = ("banana","cherry","lemon")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
#Even strings are iterable objects, and can return an iterator
mystr = "banana"
myit1 = iter(mystr)
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))

mylist = ("apple","watermelon","blueberry")
for x in mylist:
    print(x)

class Mynumbers:
    def _iter_(self):
      self.a = 1
      return self
    
    def _next_(self):
      z = self.a
      self.a += 1 
      return z

myclass = Mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class Mynumbers:
    def _iter_(self):
        self.a = 1
        return self
    def _next_(self):
        if  self.a <=20:
            x = self.a  
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = Mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
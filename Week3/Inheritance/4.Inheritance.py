#Try it yourself
#Any class can be a parent class, so the syntax is the same as creating any other class:
class Person:
    def _init_(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname,self.lname)
    
x = Person("Duman","Bayron")
x.printname()
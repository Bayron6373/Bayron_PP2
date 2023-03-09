#Try it yourself
#A variable created inside a function is available inside that function
def myf():
    x = "Hello World"
    print(x)    
myf()

def myfunction():
    x = 365
    def innerfunction():
        print(x)
    innerfunction()

myfunction()
#Global Scope
#A variable created outside of a function is global and can be used by anyone:
y = 300
def myfunc():
   print(y)

myfunc()
print(y)
#The function will print the local x, and then the code will print the global x:
x = 500
def myfunction2():
    x = 201
    print(x)
myfunction2()

print(x)
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
def myfunction3():
    global x 
    x = 300
myfunction3()
print(x)
#Also, use the global keyword if you want to make a change to a global variable inside a function.
z = 115
def myfunction4():
    global z
    z = 109
myfunction4()
print(z)
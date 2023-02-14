#Try it yourself
def my_function():
    print("Hello from London city")

my_function()

#Arguments are specified after the function name, inside the parentheses.
#You can add as many arguments as you want, just separate them with a comma 
def myfunction(firstname,lastname):
   print(firstname + " " + lastname)
myfunction("Cristiano","Ronaldo")
myfunction("Duman","Bayron")
myfunction("Frank","Lampard")
#If you try to call the function with 1 or 3 arguments, you will get an error:
#If the number of arguments is unknown, add a * before the parameter name:
def myf(*player):
    print("The best football player is" + " " + player[0]) 
myf("Cristiano Ronaldo","Leo Messi")   
#You can also send arguments with the key = value syntax.
def myfunction2(player1,player2):
    print("The best football player is" + " " + player1)

myfunction2(player1 = "Cristiano", player2 = "Leo")

def myfunction3(country = "Kazakhstan"):
    print("i am from  " + country)
myfunction3("India")
myfunction3("America")
myfunction3()
#Passing a List as an Argument
def myfunction4(food):
    for x in food:
        print(x)

food = ["meal","banana","BBQ"]
myfunction4(food)
#To let a function return a value, use the return statement:
def myfunction5(x):
    return 5*x

print(myfunction5(6))

def myf(x):
    pass

def poweroftwo(x):
    if(x>0):
        result =  x + poweroftwo(x-1)
        print(result)
    else:
        result = 0
        return result

print("\n\nRecursion Example")
poweroftwo(2)
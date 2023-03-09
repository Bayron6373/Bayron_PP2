#Try it Yourself!
#1)Python Tuples
thistuple = ["apple","cherry","grape"] #Tuples are used to store multiple items in a single variable.
print(thistuple)                       #Tuple items are ordered, unchangeable, and allow duplicate values
thistuple2 = ["apple","cherry","grape","cherry","apple"]
print(thistuple2)
print(len(thistuple2))
thistuple3 = ("grape",)
print(type(thistuple3))
#Not a tuple
thistuple4 = ("apple")
print(type(thistuple4))
thistuple5 = ("abc",15,True,"male")
print(thistuple5)
#2)Acces Tuples
thistuple6 = ("cherry","blackberry","strawberry")
print(thistuple6[2])
print(thistuple6[-1])  #we will get same output
thistuple7 = ("apple","grape","cherry","strawberry","watermelon")
print(thistuple7[2:5])
if "grape" in thistuple7:
    print("Yes,grape in this tuple") 
#3)Update Tuples
x = ("watermelon","cherry","apple")
y = list(x)
y[1] = "kiwi"
x = tuple(y)                        
print(x)
thistuple8 = ("kiwi","lemon","watermelon")
y = list(thistuple8)
y.append("orange")
thistuple8 = tuple(y)
thistuple9 = ("apple","lemon","watermelon")
y = list(thistuple9)
y.remove("lemon")
thistuple9 = tuple(y)
#4)Unpack Tuples
fruits = ("apple","banana","cherry","watermelon","apple")
(red,green,*blue) = fruits
print(red)
print(green)
print(*blue) #If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
#5)Loop Tuples
fruits2 = ("apple","blueberry","grape")
for x in fruits2:
    print(x)
thistuple4 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple4):
  print(thistuple4[i])
  i = i + 1
#6)Join Tuples
tuple1 = ("Pen","Pencil","Book")
tuple2 = ("fanta","sprite","cola")
tuple3 = tuple1 + tuple2
print(tuple3)
#we can also multiple this tuples
tuple4 = tuple1*2
print(tuple4)
#7)Tuple Methods
#count() - 	Returns the number of times a specified value occurs in a tuple
#index() - Searches the tuple for a specified value and returns the position of where it was found
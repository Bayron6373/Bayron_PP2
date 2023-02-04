#Try it Yourself!
#1)Python Dictionaries
thisdict = {
    "brand":"Toyota",
    "model":"Camry",
    "year":"2015",
    "year":"2020"#Dictionaries cannot have two items with the same key,if it happens then function will overwrite other values
}
print(thisdict["year"])
print(len(thisdict)) #To determine how many items a dictionary has, use the len() function:
print(type(thisdict))
thisdict2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict2["name"])
#2)Acces Items
thisdict3 = {
  "brand": "BMW",
  "model": "M5",
  "year": "2017"
}
x = thisdict3["model"]
print(x)
y = thisdict3.keys()
print(y)
z = thisdict3.values()
print(z)
if "model" in thisdict3:
    print("Yes")
#3)Change Items
thisdict3["year"] = 2018
print(thisdict3)
#4)Add Items
thisdict3["color"] = "red"
print(thisdict3)
thisdict3.update({"seat":"4"})
#5)Remove Items
thisdict3.pop("model")
thisdict3.popitem() #The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
del thisdict3["model"]
#6)Loop Dictionaries
for x in thisdict3:
    print(x)
    print(thisdict3[x])
for x,y in thisdict3.items():
    print(x,y)
#7)Copy Dictionaries
mydict = thisdict3.copy()
print(mydict)
#8)Nested Dictionaries
myfriends = {
    "friend1":{
        "name":"Miras",
        "year":"2005"
    },
    "friend2":{
        "name":"Zangar",
        "year":"2005"
    },
    "friend3":{
        "name":"Magzhan",
        "year":"2004"
    }
}
#Try it yourself
import json

# some JSON:
x = '{"name" : "Bayron","age":"18","city":"Almaty"}' 
# parse x:
y = json.loads(x)

#the result is a Python dictionary:
print(y["city"])

import json
x = {
    "name":"Bayron",
    "age" : "18",
    "city" : "Almaty"
}
y = json.dump(x)
print(y)

import json

print(json.dumps({"name": "Cristiano", "age": "38"}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("okay"))
print(json.dumps(35))
print(json.dumps(3.145678))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))


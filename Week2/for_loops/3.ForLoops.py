#Try is yourself
vegetables = ["Broccoli","Tomatoes","Potatoes"]
for x in vegetables:
    print(x)
for x in "banana":
    print(x)
fruits = ["apple","cherry","grape"]
for x in fruits:
    print(x)
    if x == "cherry":
     break  #or we can use order "continue" to skip 
for x in range(4):
  print(x)
else:
  print("Finally finished!")
  for x in [0,1,2]:
    pass
# having an empty for loop like this, would raise an error without the pass statement

#Try it Yourself
#1)Python Sets
set = {"apple","banana","grape"}
print(set) #the set list is unordered, meaning: the items will appear in a random order
set2 = {"apple","banana","grape","apple","grape","banana"}
print(set2) #In set duplicate values will be ignored
print(len(set2)) #To determine how many items a set has, use the len() function.
#And set items can be of any items
set3 = {"apple", "banana", "cherry"}
set4 = {1,5,6,8,9}
set5 = {True,False,True}
print(type(set4)) #We use order "type()" to determine type of set
thisset = set(("apple", "banana", "cherry"))
print(thisset)
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.
#2)Acces Set Items
thisset2 = {"apple","grape","banana"}
for x in thisset2:
    print(x)
print("banana" in thisset2)
#3)Add Set Items
set6 = {"apple","banana","grape"}
set6.add("lemon")
print(set6)
thisset4 = {"apple","lemon","grape"}
tropical = {"pineapple","watermelon","kiwi"}
thisset4.update(tropical) #To add items from another set into the current set, use the update() method.
#4)Remove Set Items 
set7 ={"banana","apple","grape"}
set7.remove("banana") #To remove an item in a set, use the remove(), or the discard() method.
set7.pop() #Remove a random item by using the pop() method
set7.clear() #clear() method  empties the set:
del set7 #The del keyword will delete the set completely:
#5)Loop Items
set8 = {"apple","banana","grape"}
for x in set8:
    print(x)
#6)Join Loops
set9 = {"apple","grape","kiwi"}
set10 = {1,2,3}
set11 = set9.union(set10) #The union() method returns a new set with all items from both sets
set9.update(set10) #The update() method inserts the items in set2 into set1:
a = {1,2,3,4}
b = {5,6,7,2}
a.intersection(b) #The intersection_update() method will keep only the items that are present in both sets.
print(a)
a.symmetric_difference(b) #The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.



#Try it Yourself
#1)Python Lists
list = ["AK-47","M4A1","AWP"]
print(list)
print(len(list))
print(type(list))
list1 = ["String","Integer","Boolean"]
list2 = [5,6,7,8]
list3 = [True,False,False,True]
print(list1)
print(list2)
print(list3)
#We can also make mix list with string,boolean,integer.
list4 = [4,"string",True]
#2)Access List items
list5 = ["Pele","Maradona","Cristiano"]
print(list5[-1]) #[-1] refers to the last item [-2] refers second last item etc.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1:4]) #Returns items that between index 1 and 4
print(thislist[2:]) #it returns just third item which "cherry"
list6 = ["apple","Murat","Abdilda","PP2"]
if "Murat" in  list6:
    print("Yes,Murat in list 6 ")
#3)Change List Items
thislist2 = ["Cherry","Apple","Banana"]
thislist2[1] = "Blackberry"
print(thislist2)
thislist2[0:2] = ["Grape"]
#4)Add List Items
list7 = ["Cristiano","Ronaldo","The"]
list7.append("GOAT") #We use order "append" to add items  
print(list7)
thislist3 = ["limon", "watermelon", "grape"]
thislist3.insert(1, "mango") #we use order "insert" to insert a list item at a specified index
print(thislist3)
thislist4 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist4.extend(tropical) #To append elements from another list to the current list, use the "extend()" method.
print(thislist4)
#5)Remove List Items
list8 = ["apple","grape","watermelon"]
list8.remove("apple")
print(list8)
list9 = ["Blackberry","Grape","Watermelon"]
list9.pop(2) #The "pop()" or "del" method removes the specified index.
list10 = ["Calculus","Statistics","Global","PP"]
list10.clear() #The clear() method empties the list.
#6)Loop Lists
list11 = ["apple","pineapple","limon"]
for x in list11:
#7)List Comprehension
 list200  = ["ice", "banana", "watermelon", "kiwi", "mango"]
newlist = []

for x in list200:
  if "a" in x:
    newlist.append(x)

print(newlist)
#8)Sort Lists
thislist5 = ["watermelon", "mango", "kiwi", "pineapple", "banana"]
thislist5.sort()
print(thislist5)
#9)Copy lists
thislist6 = ["apple", "banana", "cherry"]
mylist = thislist6.copy()
print(mylist)
#10)Join Lists
list152 = ["A", "B", "C"]
list22 = [5, 6, 7]

list33 = list152 + list22
print(list33)
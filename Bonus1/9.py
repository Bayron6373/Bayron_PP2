a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

x = abs(a1 - a2)
y = abs(b1 - b2)
if( x <= 1 and y <= 1):
    print("YES")
else:
    print("NO")
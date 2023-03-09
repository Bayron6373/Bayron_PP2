import math
n = int(input())
l = int(input())
a = l / (2 * math.tan(math.pi/n))
p = n*l
s = int(0.5*a*p)
print(s)
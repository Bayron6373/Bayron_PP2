x = lambda a : a + 20
print(x(20))    
y = lambda a,b : a*a + b
print(y(2,3))
z = lambda a,b,c : a + b + c
print(z(1,2,5))
def myfunc(n):
    return lambda a : a*n
mydoubler = myfunc(2)
print(mydoubler(11))
def myfunc2(n):
    return lambda a: a + n
mydoubler2 = myfunc2(20)
print(mydoubler2(4))
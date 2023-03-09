n = int(input())
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
    
for n in countdown(n):
    print(n)


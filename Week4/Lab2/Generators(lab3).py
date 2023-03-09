n = int(input())
def d(n):

    for num in range(n+1):
        if num % 3 == 0 and num % 4 == 0:
            yield num


for i in d(n):
    print(i)

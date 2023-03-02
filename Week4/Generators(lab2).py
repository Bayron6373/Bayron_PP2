def even_numbers(n):

    for num in range(0, n+1, 2):
        yield num

n = int(input())

even_gen = even_numbers(n)

print(*even_gen, sep=", ")

from functools import reduce

def multiply_list_numbers(lst):
    return reduce(lambda x, y: x * y, lst)

# Example usage
numbers = [2, 3, 4, 5]
result = multiply_list_numbers(numbers)
print(result) # Output: 120

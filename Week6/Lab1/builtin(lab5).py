def all_true(tup):
    return all(tup)

# Example usage
t = (True, True, False, True)
if all_true(t):
    print("All elements of the tuple are true")
else:
    print("Not all elements of the tuple are true")
# Output: Not all elements of the tuple are true
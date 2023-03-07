my_list = ["apple", "banana", "cherry", "date"]
filename = "path/to/file.txt"

with open(filename, 'w') as f:
    for item in my_list:
        f.write("%s\n" % item)

print(f"The list has been written to {filename}.")


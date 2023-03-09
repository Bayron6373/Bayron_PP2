filename = "path/to/file.txt"
num_lines = 0

with open(filename, 'r') as f:
    for line in f:
        num_lines += 1

print(f"The number of lines in {filename} is {num_lines}.")

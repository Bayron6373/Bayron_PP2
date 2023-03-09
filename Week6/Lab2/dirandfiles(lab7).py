source_file = "path/to/source/file.txt"
destination_file = "path/to/destination/file.txt"

with open(source_file, 'r') as f:
    content = f.read()

with open(destination_file, 'w') as f:
    f.write(content)

print(f"The contents of {source_file} have been copied to {destination_file}.")

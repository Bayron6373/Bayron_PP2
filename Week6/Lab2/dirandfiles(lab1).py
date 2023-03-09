import os

path = "/path/to/directory"

print("List of directories:")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

print("\nList of files:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

print("\nList of directories and files:")
for item in os.listdir(path):
    print(item)
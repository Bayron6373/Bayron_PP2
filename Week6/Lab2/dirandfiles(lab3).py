import os

path = "/path/to/file"

if os.path.exists(path):
    print(f"{path} exists.")
    dirname = os.path.dirname(path)
    print(f"The directory portion of the path is {dirname}.")
    filename = os.path.basename(path)
    print(f"The filename portion of the path is {filename}.")
else:
    print(f"{path} does not exist.")

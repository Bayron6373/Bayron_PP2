import os

path = "/path/to/file/or/directory"

# Check if the path exists
if os.path.exists(path):
    print(f"{path} exists.")

    # Check if the path is readable
    if os.access(path, os.R_OK):
        print(f"{path} is readable.")
    else:
        print(f"{path} is not readable.")

    # Check if the path is writable
    if os.access(path, os.W_OK):
        print(f"{path} is writable.")
    else:
        print(f"{path} is not writable.")

    # Check if the path is executable
    if os.access(path, os.X_OK):
        print(f"{path} is executable.")
    else:
        print(f"{path} is not executable.")

else:
    print(f"{path} does not exist.")

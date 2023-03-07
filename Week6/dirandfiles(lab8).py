import os

path = "path/to/file"

if not os.path.exists(path):
    print(f"{path} does not exist.")
elif not os.access(path, os.F_OK):
    print(f"{path} cannot be accessed.")
elif not os.access(path, os.W_OK):
    print(f"{path} is not writable.")
elif not os.access(path, os.R_OK):
    print(f"{path} is not readable.")
else:
    os.remove(path)
    print(f"{path} has been deleted.")

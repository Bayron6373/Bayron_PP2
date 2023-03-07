import string

# Generate a list of uppercase letters
letters = list(string.ascii_uppercase)

# Iterate through the letters and create a file for each one
for letter in letters:
    filename = f"{letter}.txt"
    with open(filename, 'w') as f:
        f.write(f"This is the file for letter {letter}.\n")
    print(f"{filename} has been created.")

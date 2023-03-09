def is_palindrome(string):
    return string == string[::-1]

# Example usage
text = "racecar"
if is_palindrome(text):
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
# Output: racecar is a palindrome

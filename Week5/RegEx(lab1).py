import re

# define the pattern using regular expression syntax
pattern = r'a[b]*'

# example strings to test against the pattern
test_strings = ['ab', 'a', 'abbb', 'ac', 'abc']

# iterate over the test strings and print whether they match the pattern or not
for test_string in test_strings:
    if re.fullmatch(pattern, test_string):
        print(f"{test_string}: matches pattern")
    else:
        print(f"{test_string}: does not match pattern")

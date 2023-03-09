import re


pattern = r'a[b]*'


test_strings = ['ab', 'a', 'abbb', 'ac', 'abc']


for test_string in test_strings:
    if re.fullmatch(pattern, test_string):
        print(f"{test_string}: matches pattern")
    else:
        print(f"{test_string}: does not match pattern")

import re


pattern = r'a[b]{2,3}'


test_strings = ['ab', 'abb', 'abbb', 'ac', 'abc', 'abbbb']


for test_string in test_strings:
    if re.fullmatch(pattern, test_string):
        print(f"{test_string}: matches pattern")
    else:
        print(f"{test_string}: does not match pattern")

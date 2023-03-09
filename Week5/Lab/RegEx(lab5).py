import re


pattern = r'a.*b$'


test_strings = ['ab', 'acb', 'abc', 'accb', 'adb']


for test_string in test_strings:
    if re.search(pattern, test_string):
        print(f"{test_string}: matches pattern")
    else:
        print(f"{test_string}: does not match pattern")

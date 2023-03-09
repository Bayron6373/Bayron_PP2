import re


string_to_split = "ThisIsAStringToSplitAtUpperCaseLetters"


split_string = re.findall('[A-Z][^A-Z]*', string_to_split)

print("String to split:", string_to_split)
print("Split string:", split_string)

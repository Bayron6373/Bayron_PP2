import re


string_to_modify = "ThisIsAStringToInsertSpacesBetweenWordsStartingWithCapitalLetters"


modified_string = re.sub(r"([a-z])([A-Z])", r"\1 \2", string_to_modify)


print("Original string:", string_to_modify)
print("Modified string:", modified_string)

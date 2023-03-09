import re


snake_case_string = "this_is_a_snake_case_string"

words = snake_case_string.split('_')

title_case_words = [word.title() for word in words]

camel_case_string = "".join(title_case_words)

camel_case_string = camel_case_string[0].lower() + camel_case_string[1:]

print("Snake case string:", snake_case_string)
print("Camel case string:", camel_case_string)

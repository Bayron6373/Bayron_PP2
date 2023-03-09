import re


camel_case_string = "ThisIsACamelCaseStringToConvert"


snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()


print("Original string:", camel_case_string)
print("Snake case string:", snake_case_string)

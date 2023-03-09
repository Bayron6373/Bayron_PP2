import re


pattern = r'[ ,.]'


text = 'This is a comma, space. and dot-separated string.'


new_text = re.sub(pattern, ':', text)


print(f"Original text: {text}")
print(f"Modified text: {new_text}")

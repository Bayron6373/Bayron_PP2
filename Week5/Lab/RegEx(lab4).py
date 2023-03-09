import re


pattern = r'[A-Z][a-z]+'


text = 'The Quick Brown Fox Jumps Over The Lazy Dog'


matches = re.findall(pattern, text)


print(matches)

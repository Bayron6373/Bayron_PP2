import re
txt = "The snow in Almath"
x = re.search("^The.*Almaty$",txt)

import re
txt = "The rain in Spain"
y = re.findall("ai",txt) #The findall() function returns a list containing all matches.
print(y)

import re
txt = "The rain in Spain"
x = re.split("\s",txt,1)
print(x)

import re
txt = "The rain in Spain"
x = re.sub("\s","9",txt)
print(x)

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

s = str(input())
first_world = s[:s.find(' ')]
second_world = s[s.find(' ') + 1:]
print(second_world + " " + first_world)
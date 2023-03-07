import time
import math

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds/1000)
    return math.sqrt(number)

result = delayed_sqrt(input(), input())
print(result)
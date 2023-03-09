import time
import math

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds/1000)
    return math.sqrt(number)

# Example usage
result = delayed_sqrt(25, 500)
print(result) # Output: 5.0 (square root of 25)

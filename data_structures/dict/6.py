"""
 Write a program to sum all the values in a dictionary, 
 considering the values will be of int type.
"""

import numbers

d = {1: 10, 2: 20, "a": "value", 3: 30}
sum =0

for value in d.values():
    is_no = isinstance(value, numbers.Number)
    if is_no:
        sum += value

print("Sum of Dict-values: ", sum)

"""
 Write a program to iterate over a dictionary 
 using for loop and
 print the keys alone, values alone and both keys and values.
"""

d = {0: 10, 1: 20, 3: 30, 4: 40}
i=1
for key, value in d.items():
    print(f"Iteration-{i}")
    print(key)
    print(value)
    print(f"{key} : {value}")
    i = i + 1

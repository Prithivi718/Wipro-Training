"""
 Write a program to check if 
 a given key already exists in a dictionary.
"""

d = {0: 10, 1: 20, 3: 30, 4: 40}

key = int(input("Enter a value: "))

if key in d.keys():
    print("Key found")
else:
    print("No key found")
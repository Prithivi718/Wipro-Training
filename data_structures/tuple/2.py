"""
 Write a program to check whether 
 an element exists in a tuple or not.
"""

tup = tuple(input("enter any values by space: ").split(" "))
print(tup)

value = input("Enter a value to find in above tuple: ")

if value not in tup:
    print("No value found")
else:    
    print(f"Value found: {tup[tup.index(value)]}")
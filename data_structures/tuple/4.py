"""
 Write a program to find the index of an item in a tuple.
"""
tup = tuple(input("enter any values by space: ").split(" "))
print(tup)

value = input("Enter a value to find in above tuple: ")

if value not in tup:
    print("No value found")
else:    
    print(f"Value found at index: {tup.index(value)}")

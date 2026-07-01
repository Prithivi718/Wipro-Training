"""
 Write a program to remove a given item from the set.
"""
set_input = set(input("Enter values by space: ").split(" "))

print("Set Input: ", set_input)

rem = input("Enter element to remove from above set: ")

set_input.discard(rem)
print("Removed value from set: ", set_input)
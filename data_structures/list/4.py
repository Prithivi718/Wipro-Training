"""
 Write a program to print the number of occurrences 
 of a specified element in a list.
"""


n = [1,2,3,3,4,1,5,2,5,6,6,3,2,1,5,4,4]

try:
    num = int(input("Enter a number to count occurences (1-6): "))

    if num not in n:
        raise ValueError(f"Value {num} not in list")
    
    count = n.count(num)
    print(f"The count of {num} is: {count}")
    
except ValueError as e:
    print(e)

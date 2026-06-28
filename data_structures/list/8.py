"""
 Write a program to remove the 
 first occurrence of a specified element from a list.
"""


n = [1, 2, 3, 4, 4, 5, 6]
print(n)
num = int(input("Enter the number in the list: "))

try:
    if num not in n: 
        raise ValueError("Value not in list")
    
    n.remove(num)

    print("Removed the first occurence: ", n)

except ValueError as e:
    print(e)


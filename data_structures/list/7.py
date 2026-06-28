"""
  Write a program to remove the item from 
  a specified index in a list.
"""

from multiprocessing import Value


n = [1, 2, 3, 4, 5, 6]
l = len(n)

try:
    index = int(input("Enter index position (0-5): "))

    if index > (l-1):
        raise ValueError("Index out of range")

    remove = n.pop(index)

    print(f"Removed item: {remove}")
    print(f"List: {n}")


except ValueError as e:
    print(e)

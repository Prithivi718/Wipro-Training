"""
 Write a program to count the 
 number of upper and lower case letters in a String.
"""

name = input("Enter your name: ")
upper = 0
lower = 0

for ch in name:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print(f"Upper count: {upper}\nLower count: {lower}")
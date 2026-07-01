"""
 Write a program that will check whether 
 a given String is Palindrome or not.
"""

s = input("Enter a palindrome string: ").lower()
if s == s[::-1]:
    print("Palindrome")
else: 
    print("Not palindrome")
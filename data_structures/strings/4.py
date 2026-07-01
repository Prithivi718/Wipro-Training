"""
Given a string, if the first or last character is 'x', 
return the string without those 'x' character, 
else return the string unchanged. 

If the input is "xHix", then output is "Hi".
"""

s = input("Enter a string: ")

if s[0].lower() == "x" and s[-1].lower() == "x":
    print(s[1: len(s)-1])
else:
    print(s)
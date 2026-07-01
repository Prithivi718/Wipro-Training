"""
 Given a string and an integer n, return a string made of n 
 repetitions of the last n characters of the string. 
 You may assume that n is between 0 and the 
 length of the string inclusive. 
 
 For example if the inputs are “Wipro” and 3, then 
 the output should be “propropro”.
"""

s = input("Enter a string: ").strip()
n = int(input(f"Enter a number from index: (1 - {len(s)}): "))

i = n-1

if i > len(s) - 1:
    print("Invalid number to continue")

print(s[i:] * n)
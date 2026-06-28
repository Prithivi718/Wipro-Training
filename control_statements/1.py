#  Write a program to check if a given number
#  is Positive, Negative, or Zero.

n = int(input("Enter any number: "))

res = "Positive" if n > 0 else "Zero" if n == 0 else "Negative"
print(res)
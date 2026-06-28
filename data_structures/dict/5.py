"""
  Write a program to prepare a dictionary 
  where the keys are numbers between 1 and 15 (both included)
  and the values are square of the keys.
"""

sq = dict()

for i in range(1, 16):
    sq[i] = i**2

for key, value in sq.items():
    print("Square values")
    print(f"{key}: {value}")
"""
** Lambda functions: **

Syntax: lambda arg-list: expression

Lambda function for biggest of two values

"""
big = lambda a,b : max(a,b)

print(f"Big of two numbers: 2 & 3: {big(2,3)}")

"""
** Filter ** 
Syntax: filter (func, sequence)
It will filter from a given sequence of values based on a condition

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] filter out even numbers

"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
even = list(filter(lambda l1: [value for value in l if value%2==0], l))
print(even(l))


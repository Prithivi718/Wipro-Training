numbers = [1, 2, 3, 4, 5, 6, 7]

result = {x: x**3 for x in numbers if x % 2 != 0}

print(result)
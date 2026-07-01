"""
Write a program to replace last value of tuples 
in a list to 100.  
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""
data = input("Enter tuples (comma-separated): ")

nested_tup_l = [
    tuple(map(int, t.split()))
    for t in data.split(",")
]
result = list()

print(nested_tup_l)

for i in range(len(nested_tup_l)):
    new_tup = []
    for j in range(len(nested_tup_l[i])):
        if j == len(nested_tup_l[i]) - 1:
            new_tup.append(100)
        else:
            new_tup.append(nested_tup_l[i][j])
    result.append(tuple(new_tup))

print("Replaced list-tup: ", result)
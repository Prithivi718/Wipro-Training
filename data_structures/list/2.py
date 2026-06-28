"""
APpend value to list
"""

n = [1, 2, 3, 4, 5]
print("List: ", n)

num = int(input("Enter a num to append to end of the list: "))
n.append(num)


for i in range(len(n)):
    print(f"Index-{i}: {n[i]}")
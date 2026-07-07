n = int(input("Enter number of lines: "))

file = open("sample.txt", "r")

for i in range(n):
    print(file.readline(), end="")

file.close()
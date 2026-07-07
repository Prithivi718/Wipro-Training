file = open("sample.txt", "r")

lines = file.readlines()

line_list = []

for line in lines:
    line_list.append(line.strip())

print(line_list)

file.close()
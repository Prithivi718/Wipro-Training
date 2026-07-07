word = input("Enter word to search: ")

file = open("sample.txt", "r")

content = file.read().split()

count = content.count(word)

print("Frequency:", count)

file.close()
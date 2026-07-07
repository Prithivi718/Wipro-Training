text = input("Enter text to append: ")

file = open("sample.txt", "a")

file.write("\n" + text)

file.close()

print("Text appended successfully")
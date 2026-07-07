file = open("sample.txt", "r")

words = file.read().split()

longest_word = max(words, key=len)

print("Longest word:", longest_word)

file.close()
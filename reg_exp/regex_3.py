import re

sentence = "A, very    very; irregular_sentence"

words = re.findall(r'\w+', sentence)

result = " ".join(words)

print(result)
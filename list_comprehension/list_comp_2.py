import string

alphabet_dict = {char: index+1 for index, char in enumerate(string.ascii_lowercase)}

print(alphabet_dict)
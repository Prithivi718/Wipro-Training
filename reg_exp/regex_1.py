import re

strings = ['789', '123', '004']

for s in strings:
    if re.fullmatch("[0-7]+", s):
        print(s, "-> Octal")
    else:
        print(s, "-> Not Octal")
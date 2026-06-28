s1 = input("Enter string-1: ")
s2 = input("Enter string-2: ")


# split_letter = [a+b for a, b in zip(s1, s2)]
# print(split_letter)

# result = "".join(split_letter)
# print(result)

result = ""

s1_len = len(s1)
s2_len = len(s2)
max_len = max(s1_len, s2_len)

for i in range(max_len):
    if i < s1_len:
        result += s1[i]
    if i < s2_len:
        result += s2[i]

# if s1_len > s2_len:
#     result += s1[:s1_len-1]

# if s2_len > s1_len:
#     result += s2[:s2_len-1]

print("Result of merged strings: ", result)


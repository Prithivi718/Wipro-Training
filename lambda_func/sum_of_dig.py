n = 976592

s_n = str(n)
temp = s_n

while True:

    if len(temp) == 1:
        print(f"Sum of {n}: {sum}")
        break

    sum = 0   

    for digit in temp:
        sum += int(digit)
    
    temp = str(sum)

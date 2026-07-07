numbers = [10, -5, 8, -12, 15, -7, 22, -9, 3, -1]

try:
    index = int(input("Enter index (0-9): "))

    value = numbers[index]

    if value >= 0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Error: Invalid index")

except ValueError:
    print("Error: Please enter a valid number")
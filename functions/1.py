def sum_list(lst):
    total = 0

    for i in lst:
        total += i

    return total


numbers = [8, 2, 3, 0, 7]

print("Sum =", sum_list(numbers))
try:
    filename = input("Enter the file name: ")

    file = open(filename, "r")

    lines = file.readlines()
    file.close()

    total_items = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        parts = line.split()

        # Check discount line
        if parts[0].lower() == "discount":
            discount = int(parts[1])

        else:
            item_name = parts[0]
            item_price = parts[1]

            if item_price.lower() == "free":
                free_items += 1
            else:
                amount += int(item_price)
                total_items += 1

    final_amount = amount - discount

    print("No of items purchased:", total_items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("Error: File not found")

except ValueError:
    print("Error: Invalid data in file")

except Exception as e:
    print("Exception:", e)

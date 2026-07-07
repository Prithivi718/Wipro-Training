n = int(input("Enter the no of people u wanna talk about: "))

d = dict()

for i in range(n): 
    name = input("Enter the name of person: ")
    fact = input(f"Enter the intresting fact about {name}: ")

    d[name] = fact

for key, value in d.items():
    print(f"{key}: {value}")

change_fact = input("Enter name of person, to change the fact: ")

if change_fact in d.keys():
    fact = input("Enter the modify fact: ")
    d[change_fact] = fact

name = input("Add the name of person: ")
fact = input(f"Add the intresting fact about {name}: ")

d[name] = fact

print("Modified dict: ")

for key, value in d.items():
    print(f"{key}: {value}")

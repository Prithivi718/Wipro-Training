marks = dict()

n = int(input("Enter the Number of student records: "))

for i in range(n):
    name = input("Enter the student name: ")
    mat = int(input("Enter the Maths Mark: "))
    soc = int(input("Enter the Social Mark: "))
    sci = int(input("Enter the Science Mark: "))

    marks[name] = [mat, soc, sci]

for key, value in marks.items():
    print(f"{key}: {value}")

stud = input("Enter the student name to find average: ")

if stud in marks.keys():
    avg = sum(marks[stud]) / len(marks[stud])
    print(f"Average of {stud} is: {avg}")
else:
    print("No student data found")
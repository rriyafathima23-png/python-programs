students = {
    "Riya": 85,
    "Anu": 92,
    "Rahul": 78
}

key = input("Enter student name: ")

if key in students:
    print("Key exists")
else:
    print("Key does not exist")
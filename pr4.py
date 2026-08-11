students = {
    "Riya": 85,
    "Anu": 92,
    "Rahul": 78
}

highest = max(students, key=students.get)

print("Top Student:", highest)
print("Highest Mark:", students[highest])
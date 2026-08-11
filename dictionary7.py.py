students = {
    "Riya": 85,
    "Anu": 92,
    "Rahul": 78
}

sorted_dict = dict(sorted(students.items(), key=lambda x: x[1]))

print(sorted_dict)
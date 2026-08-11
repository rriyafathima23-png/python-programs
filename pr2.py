marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

if marks >= 35 and attendance >= 75:
    print("Student Passed")
else:
    print("Student Failed")
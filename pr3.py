age = int(input("Enter your age: "))
license_id = input("Do you have a license ID? (yes/no): ")

if age >= 18 and license_id == "yes":
    print("Eligible for driving.")
else:
    print("Not eligible for driving.")
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 4, 7]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)
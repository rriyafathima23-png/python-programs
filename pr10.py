numbers = [1, 2, 2, 3, 1, 4, 2, 5, 3]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Element frequencies:")
for key in frequency:
    print(key, ":", frequency[key])
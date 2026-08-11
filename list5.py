numbers = [12, 45, 7, 89, 23, 56, 90, 34, 18, 67]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
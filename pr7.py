numbers = [12, 45, 7, 89, 23, 56, 90, 34]

largest = second = -999999

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)
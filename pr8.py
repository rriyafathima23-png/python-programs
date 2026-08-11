list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merged = list1 + list2
result = []

for item in merged:
    if item not in result:
        result.append(item)

print("Merged list:", result)
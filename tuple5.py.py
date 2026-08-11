t = (10, 20, 30)

lst = list(t)

num = int(input("Enter new element: "))
lst.append(num)

t = tuple(lst)

print("New tuple:", t)
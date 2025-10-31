import re

number = input("Enter an Integer: ")
pattern = r"\d{1,}"
matched = re.match(pattern, number)

print(matched)

arr = [17, 12, 21, 8, 13, 4, 11, 16]

print(arr.sort(reverse=True))
print(arr.sort())

arr.sort(key= lambda x: sum(int(y) for y in str(x)))
print(arr)
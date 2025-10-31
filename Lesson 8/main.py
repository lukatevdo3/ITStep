# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# print(set1.difference(set2))
# print(set1 - set2)
# print(set1.union(set2))
# print(set1^set2)
# print(set1.intersection(set2))

# arr = input("Enter a Numbers: ").split(" ")

# print(arr)


# arr = map(eval, input("Enter a Numbers: ").split(" "))
# print(arr, type(arr))
# print(*arr)
# print(list(arr))

# arr = list(map(eval, input("Enter a Numbers: ").split(" ")))
# print(arr)

# def func(num: int) -> None:
#     print(num ** 3)


# func(3)

# def func(num, power):
#     print(num ** power)

# func(3, 2)

# def func(num, power, number = 0):
#   print(num ** power)
#   print(number)

#   print(str1, "Local Variable ", func.__name__)


# str1 = "ZERO ZERO ZERO"
# func(3, 4)
# print(str1, "Global Variable", __name__)


def func(num, power, number = 0):
  print(num ** power)
  print(number)
  str1 = "Python Is Funny!"
  print(str1, "Local Variable ", func.__name__)


str1 = "ZERO ZERO ZERO"
func(3, 4)
print(str1, "Global Variable", __name__)



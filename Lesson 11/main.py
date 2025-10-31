# def main(a, b):

#     return a if a>b else b

# print(main(8, 5))

# func1 = lambda num: num - 100 if num > 100 else num + 100

# print(func1(35))
# print(func1(100))

# func1 = lambda num: f"Number is: {num - 100 if num > 100 else num + 100}"

# print(func1(35))

# arr = [1, 2, 3, 4, 5, 6, 7, "text", False]

# num = list(map(lambda x: 2 * x, arr))
# print(num)

# num1 = list(filter(lambda y : type(y) == int, arr))
# print(num1)

# arr1 = ["1", "2", "3"]

# num3 = list(map(eval, arr1))
# print(num3)

# num4 = list(map(lambda x : eval(x), arr1))
# print(num4)

# arr2 = [1, 2, 3, 4, 5]
# arr3 = ['a', 'b', 'c', 'd']

# print(list(zip(arr2, arr3)))
# print(*zip(arr2,arr3))
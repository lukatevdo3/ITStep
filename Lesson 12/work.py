# lambda_func = lambda x: x

# print(lambda_func(4))

# l_func1 = lambda x, y: x + y

# print(l_func1(5, 10))

# l_func1 = lambda x = 10, y = 5: x + y

# print(l_func1())

# lst = [lambda args1 = x: args1 * 10 for x in range(1, 11)]

# print(lst)

# for func in lst:
#     print(func())

# lst2 = [(lambda args1, args2: args1*args2)(x, y) for x in range(1, 11) for y in range(1, 11)]

# print(lst2)

# import functools

# lst3 = [1, 2, 3, 4, 5, 6, 7]

# sum_of_lists = functools.reduce(lambda a, b: a + b, lst3)

# print(sum_of_lists)

# factorial = functools.reduce(lambda a, b: a * b, range(1, 6))

# print(factorial)

# from functools import partial

# def mult(a, b):
#     return a * b

# multiplication = partial(mult, a = 5)
# print(multiplication(b = 10))

# from functools import reduce


# lst4 = [(lambda x: x)(x)for x in range(1, 11)]

# reduction = reduce(lambda x, y: x-y, lst4)
# print(reduction)

# lst5 = [(lambda x: x)(x)for x in range(1, 7)]

# mapping = list(map(lambda x: x**3, lst5))

# def mapping2(x):
#     return x ** 3

# mapping1 = list(map(mapping2, lst5))

# print(mapping1)

# lst6 = [(lambda x: x)(x)for x in range(1, 15)]

# filtering = list(filter(lambda x: x%2 == 0, lst6))

# print(filtering)

'''
filter funtion always takes his first argument as
a function which should return boolean value

''' 

# lst7 = [1, 2, 3]
# lst8 = [4, 5, 6]

# zipped = list(zip(lst7, lst8))
# print(zipped)

# zipped1 = list(x+y for x,y in zip(lst7, lst8))
# print(zipped1)

# try:
#     number1 = int(input("Enter Number: "))
#     number2 = int(input("Enter Number: "))
#     print(number1/number2)
# except:
#     print("Error")

# print("Try Except Finished")

# try:
#     number1 = int(input("Enter Number: "))
#     number2 = int(input("Enter Number: "))
#     print(number1/number2)
# except ZeroDivisionError:
#     print("Cannot divide by zero...")
# except ValueError:
#     print("Wrong Value Input!")
# except Exception as ex:
#     print(ex)
# else:
#     print("Try Except Finished Successfully")
# finally:
#     print("Try Except Finished!")  
 


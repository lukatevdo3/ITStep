# def my_func(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)


# arr = [1, 3, 4, 5, 6, 11, 0.9]
# dict1 = {"name":"kise", "age":14, "sport": "basketball"}

# my_func(*arr, **dict1)

# def my_func(arg1, arg2, arg3, name = '', age = 0, sport = ''):
#     print(arg1, arg2, arg3)
#     print(name, age, sport)


# arr = [1, 3, 4]
# dict1 = {"name":"kise", "age":14, "sport": "basketball"}

# my_func(*arr, **dict1)

# def recursive(value):
#     print(value)

#     recursive(value + 1) #infinite function

# recursive()

def recursive(value):
    print(value)

    if value < 4:
        recursive(value + 1) #infinite function



recursive(1)

# def count_integers(*args):
#     count = 0

#     for i in args:
#         if type(i) in (int, float) and i > 0:

#             count += 1
    
#     return count

# # ===================

# arr = [1.2, 5.8, 2.56, "1.58", True, 10, False, -8]

# result = count_integers(*arr)
# print(result)


# def my_func():
#     local = "local"

#     print(local)

# local = "global"

# my_func()

def outer(N):
    a, b , arr = 1, 0, []
    

    def fibo():
        print(a, b, arr)
    
    fibo()

outer(10)






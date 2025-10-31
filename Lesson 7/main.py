# test_tuple = (1, "hello", .5, [1, 2, 3, 4])
# test_tuple[-1][1] = 10

# print(test_tuple)

# a, b, c ,d = test_tuple
# print(a,b,c,d, sep = "\n")

# a, b, *c = test_tuple
# print(a, b , c, sep = '\n')

# args = range(1, 10)

# print(args)
# print(*args)
# print(list(args))

# args = range(4, 59, 3)

# args = tuple(i for i in args if i % 2 == 1)
# print(args)

# arr = [19, 28, 20, 15, 22]
# print(enumerate(arr))
# print(*enumerate(arr))

# for i in enumerate(arr):
#     print(i)

# print('\n')

# for i, num in enumerate(arr):
#     print(i, num)

# cells = ((row, col) for row in range (1,4) for col in range(1,3))

# for cell in cells:
#     print(cell)

# cells = ((row, col) for row in range (1,4) for col in range(1,3))

# for i, cell in enumerate(cells, 1):
#     if i % 2 != 0:
#       print(cell, end='\t')
#     else:
#        print(cell)


# cells = [(row, col) for row in range(1,4) for col in range(1,3)]

# for i, cell in enumerate(cells, 1):
#     if i % 2 != 0:
#         print(cell, end = "\t")
#     else:
#         print(cell)
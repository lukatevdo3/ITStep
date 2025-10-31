import os

# def decorator(func):
#     def wrapper(*args):
#         a = args[1]**2
#         func(args[0], a)

#     return wrapper

# @decorator
# def function1(balance, money):
#     y = 0
#     for i in balance:
#         y += i
#     print(y, money)


# list1 = [1, 2, 3, 4, 5]

# function1(list1, 2)

# file = open("files1/text.txt", mode = "w")
# file.write("Kise #4")
# file.close()

# file = open("text.txt", mode = "w")
# file.writelines(["1\n", "2\n", "3\n"])
# file.close()

# file = open("text.txt", mode = "a")
# file.write("\nKise #3")
# file.close()


# file = open("text.txt", mode = "r")
# print(file.readlines())
# file.close()    

# with open("text.txt", "r") as file:
#     file.read()

# with open("text.txt", "r+") as file:
#     print(file.readable())
#     print(file.writable())

# import os

# os.remove("text.txt")

'''

JSON

'''

import json

# dict1 =''' {
#     "names": [
#         {
#             "firstname": "Jim",
#             "age": 32
#         },
#         {
#             "firstname": "Fred",
#             "age": 32
#         },
#         {
#             "firstname": "Bob",
#             "age": "28"
#         },
#         {
#             "firstname": "Joe",
#             "age": 40
#         }
#     ]
# }
# '''

# data = json.loads(dict1) # # loads add that dict1 to json file called data

# for i in data["names"]:
#     print(i["firstname"])


# print(data["names"])

# os.mkdir("files")

# folder = "files"

# user_info = {"name" : "John Smith", "age" : 57, "active" : True} 

# with open(folder + "/text1.txt", mode = "w", encoding = "utf-8") as file:
#     # file.write(str(user_info)) # # it will work but its not appropriate since it will be troublesome

#     file.write(json.dumps(user_info, indent = 2)) # # it is written inside file.write() because it just converts python data to json format but do not add it anywhere
#     # boolean type converts to lowercase


# folder = "files"

# with open(folder + "/text1.txt", mode = "r", encoding = "utf-8") as file:
#     data = file.read()

# print(data)
# print(type(data))

'''
when you write json.loads or json.dumps you should always use file.read()
or file.write() functions because without it it doesnt save output it just
converts it 

'''

# folder = "files"

# with open(folder + "/text1.txt", mode = "r", encoding = "utf-8") as file:
#     data = json.loads(file.read())

# print(data)
# print(type(data))
# print(data[0]["name"])

# folder = "files"
# user_info = {"name" : "John Smith", "age" : 57, "active" : True} 

# with open(folder + "/text1.txt", mode = "a", encoding = "utf-8") as file:
#     # file.write(str(user_info)) # # it will work but its not appropriate since it will be troublesome

#     file.write(json.dumps(user_info, indent = 2))

from students import create_json_file
from students import write_json_file
from students import read_json_file
from students import update_json_file
from pprint import pp


students = [
    {'id' : 14, 'name' : 'Giorgi', 'score' : 84},
    {'id' : 21, 'name' : 'Lasha', 'score' : 69},
    {'id' : 54, 'name' : 'Nika', 'score' : 61},
    {'id' : 63, 'name' : 'Nia', 'score' : 78},
    {'id' : 89, 'name' : 'Dato', 'score' : 92},
    {'id' : 94, 'name' : 'Marika', 'score' : 71},
]

file_path = create_json_file("files/jsons", "data")

# write_json_file(file_path, students)

# file_content = read_json_file(file_path)

# pp(file_content)


# new_student = {'id' : 61, 'name' : 'Keti', 'score' : 89}

# data = update_json_file(file_path, new_student)
# pp(data)









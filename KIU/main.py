# # # 1

# name = input("Enter your name: ")
# print("Hello " + name + "!")

# #Add two numbers

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# sum1 = num1 + num2

# print(sum1)

# #Square of Num

# print((sum1)**2)

# #if/else/elif Statement

# if sum1<=0:
#     print("Ugrela")

# number = int(input("Enter a number: "))

# if number > 0:
#     print("The Number is Positive!")
# elif number <0:
#     print("The Number is Negative!")
# else:
#     print("The Number is Zero")


# #Check if the number is even or odd

# number1 = int(input("Enter your number: "))

# if number1 % 2 == 0:
#     print("Even")
# elif number1 % 2 != 0:
#     print("Odd") 
# else:
#     print("Zero")

# #Print numbers from 1 to 10
# num3 = range(1, 11)
# print(*num3)

# for i in range(1, 11):
#     print(i, end = ' ')

# sum = 0
# for i in range(1, 101):
#     sum += i


# print(sum)


# char1 = input("Enter A String: ")

# sum2 = 0

# for i in char1:
#     if i in ("a", "e", "i", "o", "u"):
#         sum2 += 1

# print(sum2)

# num5 = int(input("number: "))

# for i in range(1, num5+1):
#     print(num5, end = ' ')
#     num5 -= 1   


# # # 2

# i = int(input("Enter a Number: "))

# if i in range(1, 101):
#     if i >= 90:
#         print(f"A")
#     elif i >= 80:
#         print(f"B")
#     elif i >= 70:
#         print(f"C")
#     elif i >= 60:
#         print(f"D")
#     elif i >= 0:
#         print(f"F")
# else:
#     print("Invalid score")


# password = input("Enter Your Password: ")

# if len(password) < 6 or ' ' in password or ("password" or "123456" or "qwerty") in password:
#     print("Invalid Password!")
# else:
#     if 10 > len(password) >= 8:
#          for i in password:
#              if i.isdigit():
#                  print("Moderate")
#     elif 12 >= len(password) >= 10:
#         for i in password:
#             if i.isdigit() or i.upper() or i.lower():
#                 print("Strong")

# password = input("Enter Your Password: ")

# has_upper = False
# has_digit = False
# has_lower = False
# has_special = False
# special = "!@#%&_-+"

# for i in password:
#     if i.isupper():
#         has_upper = True
#     if i.islower():
#         has_lower = True
#     if i.isdigit():
#         has_digit = True
#     if i in special:
#         has_special = True


# 3

attempts = 3
password = "password123"

while attempts > 0:

    your_password = input("Enter a Password: ")

    if your_password != password:
        print("Incorrect password!")
        attempts -= 1
    else:
        print("Correct password!")
        break











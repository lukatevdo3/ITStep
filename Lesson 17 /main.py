# class Student:
#     def student():
#         ...

#     def avg_scores():
#         ...

    

# st1 = Student()

# print(st1)
# print(type(st1))

# class Student:
#     def student(self):
#         ...

#     def avg_scores(self):
#         ...

    

# st1 = Student()

# print(st1)
# print(type(st1))
# print(st1.student())

# class Student:
#     def __init__(self):
#         print("Initialize Function")

#     def student(self):
#         ...

#     def avg_scores(self):
#         ...


# st1 = Student()

# class Student:
#     def __init__(self, name, score):
#         print("Initialize Function")
#         print(name, score)

#     def student(self):
#         ...

#     def avg_scores(self):
#         ...


# st1 = Student("Luka", 19)

# class Student:
#     def __init__(self, name, grade = 0):
#         print(name, grade)

#     def student(self):
#         print("Luka Tevdoradze")

#     def avg_scores(self):
#         ...


# st1 = Student()



# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade 

#     def student(self):
#         print("Name: ", self.name)

#     def avg_scores(self):
#         ...


# st1 = Student("luka", 87)
# st2 = Student("giorgi", 59)

# st1.student()
# st2.student()

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade 

#     def student(self):
#         print("Name: ", self.name)

#     def avg_scores(self):
#         ...


# st1 = Student("luka", 87)
# st2 = Student("giorgi", 59)

# print(st1.name, st1.grade)
# print(st2.name, st2.grade)

# st1.name = "110011"
# st1.grade = -5
# print(st1.name, st1.grade)


# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.__grade = grade 

#     def student(self):
#         print("Name: ", self.name)

#     def avg_scores(self):
#         ...


# st1 = Student("luka", 87)
# st2 = Student("giorgi", 59)

# print(st1.name, st1.__grade)

'''
Getters and Setters

'''

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.__grade = grade

#     def get_grade(self):
#         return self.__grade

#     def set_grade(self, new_grade):
#         self.__grade = new_grade if 0 <= new_grade <=100 else "numbers between 0 and 100"

#     def print_student_name(self):
#         print(f"name: {self.name}")

#     def avg_score(self):
#         ...


# st1 = Student("luka", 87)
# st2 = Student("nana", 59)

# print(st1.get_grade())
# st2.set_grade(50)
# print(st2.get_grade())

# print(st1._Student__grade)

# print(dir(st1), "\n")
# print(st1.__dict__)


class Computer:
    def __init__(self, price = 1000):
        self._price = price

    def set_price(self, new_price):
        self._price = new_price if new_price is type(int, float) and new_price >= 0 else print("wrong price")

    def get_price(self):
        return self.get_price
    
    def show(self):
        print(f"Retail Price: {self._price}")


comp1 = Computer(1200)

print(comp1.show())

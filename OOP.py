# OOP in Python
# to map with real world scenarios, we started using objects in code
# This is called object oriented programming

# a = 10
# b = 20

# sum = a + b
# print(sum)

# diff = a - b
# print(diff)

# for function redundancy decreases, reusability increases
# from procedural programming we moved to functional programming and now we are doing object oriented programming
# first the classes of an object then we call it object

########### Class & Object in Python ##############
# Class is a blueprint for creating objects
# Creating class
# class student:
    # Precedence of Object attr > Precedence of Class attr
    # name = "Eshat"
    # College_Name = "Notre Dame College" # Class attr
    # name = "anonymous" # Class attr

    # def __init__(self): # Default Constructor
    #     # print("adding new student in Database..")
    #     pass

    # def __init__(self, fullname, marks): # Parameterized Constructor
    #     self.name = fullname
    #     self.marks = marks
        # print("adding new student in Database..")

########## Methods ##########
# Inside the methid we have to write self
#     def welcome(self):
#         print("Welcome Student,", self.name)

#     def get_marks(self):
#         return self.marks
    
# # creating object (instance)
# s1 = student("Eshat", 100)
# # print(s1.name) # Eshat
# # print(s1.marks) # 100
# s1.welcome()
# print(s1.get_marks())

# s2 = student("Karim", 98)
# print(s2.name) # Karim
# print(s2.marks) # 98

# print(student.College_Name)

# The self parameter is a reference to the current instance of th eclass, and is used to access variables that belongs to the class
# Variables stored inside the class are called attributes
# s2 = student()
# print(s2.name)

# class Car:
#     color = "Blue"
#     brand = "Mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# Constructor
# Whenever a new object created, the constructor got called
# All classes have a function called _init_(), which is always executed when the class/object is being initiated

########## Class & Instance Attributes ##############

######## Methods ############
# The functions we use inside the class we call those methods


########### Static Method ############
# Methods that don't use the self parameter (work at class level)

# class student:
#     @staticmethod # Decorator
#     def college():
#         print("Notre Dame College, Dhaka")

################### IMPORTANT #######################
# Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user.

# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")

# car1 = car()
# car1.start()

############# Encapsulation #############
# Wrapping data and functions into a single unit (object)

############## del Keyword #############
# used to delete object properties or object itself.
# del s1.name
# sel s1

# class student:
#     def __init__(self, name):
#         self.name = name

# s1 = student("Eshat")
# print(s1.name)
# del s1.name
# print(s1.name)

# Private(like) attributes & methods
# Conceptual Implementation in Python
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # "__" makes the attributes private

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("0006-1789653", "suchi")

# print(acc1.acc_no)
# print(acc1.reset_pass())

# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()

# print(p1.welcome())

#################### Inheritance ###############
# when one class(child/derived) derives the properties & methods of another class(parent/base)

# class Car:
#     # color = "black"
#     @staticmethod
#     def start():
#         print("car started....")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# car1.start()
# print(car1.color)

# class Fortuner(ToyotaCar):
#     def __init___(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()

# Three types of Inheritance
# --> Single Inheritance
# --> Multi-level Inheritance
# --> Multiple Inheritance

# Example of Multiple Inheritance

# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

################## Super Method #####################
# class Car():
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = ToyotaCar("prius", "Electric")
# print(car1.type)

############### Class Method #####################
# A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method can't access or modify class state & generally for utility

# class Person:
#     name = "anonymous"

#     # def chaneName(self, name):
#     #     self.name = name

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Eshat")
# print(p1.name)
# print(Person.name)

########## Property Decorator ###########
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

#     # def calculatePercentage(self):
#     #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
        
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = Student(98, 97, 99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.phy)
# #stu1.calculatePercentage()
# print(stu1.percentage)

# @getter
# @setter

############ Polymorphism : Operator Overloading ##############
# print(1 + 2) #3
# print("Karim" + "Eshat") #concatenate
# print([1,2,3] + [4,5,6]) #merge

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()
num3 = num1 + num2
num4 = num1 - num2

# Dunder function mean __

# num3 = num1.add(num2)
num3.showNumber()
num4.showNumber()
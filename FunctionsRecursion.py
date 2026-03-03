# function definition
# def sum(a, b):
#     s = a + b
#     return s

# def print_hello():
#     print("Hello")

# a = 5
# b = 10
# print(sum(a, b))

# output = print_hello()
# print(output) # none value

# average of three numbers

# def avg(a, b, c):
#     average = (a + b + c) / 3
#     return average

# print(int(avg(1, 2, 3)))

# There are two types of function in a language
# Built-in function & User-defined function

# in order to print in same line
# print("Karim", end=" ")
# print("Eshat")

# Default Parameter
# def cal_prod(a = 1, b = 1): # default values come last
#     print(a * b)
#     return a * b

# cal_prod()

################## Recursion #####################
# def show(n):
#     if(n == 0): # Base case
#         return
#     print(n)
#     show(n-1)

# show(5)

# Factorial
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(3))
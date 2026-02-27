# list & tuple
# List

# marks1 = 94.4
# marks2 = 87.5
# marks3 = 95.2
# marks4 = 66.4
# marks5 = 45.1

# marks = [94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(len(marks))
# print(type(marks))
# print(marks[0])
# print(marks[1])

# python doesn't need same type of data in it's list
# we can store multiple type of data in list of python

# student = ["Karan", 21, "Dhaka"]
# print(student[0])
# student[0] = "Eshat"
# print(student)

# List Slicing
# marks = [85, 94, 76, 63, 48]
# print(marks[1:4])

# List Methods
# list = [2, 1, 3]
# list.append(4) # adds one element at the end
# print(list)
# list.sort() # sorts in ascending order. For list of strings it will prioritize alphabetical order.
# print(list)
# list.sort(reverse = True) # sorts in descending order
# print(list)
# list.reverse() # reverses list
# print(list)
# list.insert(1, 5) # insert element at index. it increases the list length
# print(list)
# list.remove(1) # first 1 will be removed
# print(list)
# list.pop(2) # removing the value of the respective index
# print(list)

# Tuples in Python
# this are like immutable sequence of values
# it's like constant list
# list is muttable
# strings are immutable
# tuples use parenthesis not square brackets

# tup = (2, 1, 3, 1)
# print(type(tup))
# print(tup[0])

tup = (1, 2, 3, 4, 2, 6, 7) # if I just surround a single value with parenthesis. It will become int type
print(tup)
print(type(tup))
print(tup[1:3])

print(tup.index(1)) # returns index of first occurrence. It returns the element's index
print(tup.count(2)) # counts total occurrences

# info = {
#     "key" : "value",
#     "name" : "Eshat",
#     "learning" : "coding",
#     "age" : 35,
#     "is_adult" : True,
#     "marks" : 94.4,
# }

# print(type(info))

# # dicts are unordered, mutable(changable) & don't allow duplicate keys
# # they are having no indexing system

# print(info["name"])
# print(info["age"])
# print(info["marks"])

# null_dict = {}
# print(null_dict)

# # new assignment, changing the value of the key
# info["name"] = "Mahmudul" # overwrite
# print(info)

# nesting
# student = {
#     "name" : "Eshat",
#     "subjects" : {
#         "Math" : 100,
#         "Chemistry" : 89,
#         "Physics" : 90
#     }
# }

# print(student)
# print(student["subjects"]["Chemistry"])

# print(student.keys()) # returns all the keys
# print(list(student.keys())) # typecasting
# print(len(student)) # number of keys inside
# print(len(list(student.keys())))
# print(student.values()) # printing the values of the keys
# print(student.items()) # returns the dict making it a tuple
# print(list(student.items())) # typecasting
# print(student.get("name")) # value of the key
# print(student["name"]) # same method to print the value
# student.update({"city" : "Dhaka"}) # can be done also by making new dictionary. Must be remembered that old keys cannot be used.
# print(student)
# print(student["name2"]) # error
# print(student.get("name2")) # no error. Prints None

# pairs = list(student.items()) # converting it to list to access the items by indexing
# print(pairs[0])

################################## Set in Python ##############################################

# set is a collection of the unordered items
# Each element in the set must be unique & immutable.

# collection = {1, 2, 3, 4 , "Karim", "Eshat"} # if there is duplicate value set will ignore that

# print(collection)
# print(type(collection))
# print(len(collection))

# collection2 = {} # empty dictionary

# for creating empty set
collection3 = set() # empty set; syntax

collection3.add(1) # adds an element
collection3.add(2)
collection3.add(3)
collection3.add((1, 2, 3))
collection3.remove(3) # removes the element
# collection3.clear() # empties the set
# collection3.pop() # removes a random value
# list cannot be added to a set
# print(collection3)

collection4 = {1, 2, 4, 5, 6}
# print(collection3.union(collection4)) # combines both set values & returns new
print(collection3.intersection(collection4)) # combines common values & returns new
# str1 = "This is a string. \nWe are creating it in python."
# str2 = 'Eshat'
# str3 = """this is a string"""

# 'this is Eshat's life'
# we cannot use apostrophy if we use single quote for strings. So, double quotes are preferrable to use.

# If I want to print one line in the next line I need to use escape sequence character.
# Escape sequence characters are characters which pushes our code to using tab, next line etc.

# print(str1)

# str1 = "Mahmudul"
# str2 = "Karim"
# str3 = str1 + str2

# print(str1[3])
# print(len(str3))
# print(str2[2])

# I cannot change the string using indexing.

#slicing
# str4 = "Karim Eshat"
# print(str4[6:len(str4)])
# if we miss the last index python will automatically understand upto the last index. It is true for the first index also

#string functions
# str = "i am studying python from ApnaCollege."
# print(str.endswith("ege."))
# print(str.capitalize()) # this function creates a copy of the previous str and changes there not in the actual one.

# print(str.replace("python", "cpp")) # this function replaces all the o to a.

# print(str.find("q")) # this function searches for the character/word and returns the first index of first time use of that character/word.
# print(str.count("from")) # this function counts how many times that character/word used inside the string.



# Conditional Statements
# light = "green"
# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")

# print("end of code")

# num = 1

# if(num > 2):
#     print("Greater than 2")
# elif(num > 3):
#     print("Greater than 3")
# else:
#     print("so small")


#Grade students based on marks
marks = float(input("How much you got?\n"))

if(marks >= 90):
    print("Grade = A")
elif(marks >= 80 and marks < 90):
    print("Grade = B")
elif(marks >= 70 and marks < 80):
    print("Grade = C")
else:
    print("Grade = D")

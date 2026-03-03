# f = open("demo.txt", "a")

# f.write("\nI want to learn React.js.")
f = open("sample.txt", "a")
f.write("I am starting with Python.")

# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
# # print(type(data))
f.close()

# 'r' --> open for reading (default)
# 'w' --> open for writing, truncating the file first
# 'x' --> create a new file and open it for writing
# 'a' --> open for writing, appending to the end of the file if it exists
# 'b' --> binary mode(default)
# 't' --> text mode (default)
# '+' --> open a disk file for updating (reading and writing)

# Deleting a File
# using the OS module

import os
os.remove("sample.txt")
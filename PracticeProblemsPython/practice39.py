count = 0

with open("practice.txt", "r") as f:
    data = f.read()
    # print(data)

# num = data.split(",")
# for val in num:
#     if(int(val) % 2 == 0):
#         count += 1

# print(count)

num = ""

for i in range(len(data)):
    if(data[i] == ","):
        if(int(num) % 2 == 0):
            count += 1
        num = ""
    else:
        num += data[i]


# Check last number
if num != "":
    if int(num) % 2 == 0:
        count += 1

print(count)
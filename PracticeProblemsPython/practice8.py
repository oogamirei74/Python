num1 = int(input("Input your first number: "))
num2 = int(input("Input your second number: "))
num3 = int(input("Input your third number: "))

if(num1 > num2 and num1 > num3):
    print("First number is greater amongst the three")
elif(num2 > num1 and num2 > num3):
    print("Second number is greater amongst the three")
else:
    print("Third number is greater amongst the three")
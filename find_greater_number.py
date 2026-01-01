num1=int(input("Enter first number\t"))
num2=int(input("Enter second number\t"))
num3=int(input("Enter third number\t"))
if num1>num2:
    if num1>num3:
        print(num1,":first number is greater number\t")
    else:
        print(num3,":third number is greater number\t")
elif num2>num1:
    if num2>num3:
        print(num2,":second number is greater number\t")
    else:
        print(num3,":third number is greater number\t")
else:
    print("all NUMBER ARE EQUAL ")

# using functions
def is_greater(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(num1,":first number is greater number\t")
        else:
            print(num3,":third number is greater number\t")
    elif num2>num1:
        if num2>num3:
            print(num2,":second number is greater number\t")
        else:
            print(num3,":third number is greater number\t")
    else:
        print("all NUMBER ARE EQUAL ")
num1=int(input("Enter first number\t"))
num2=int(input("Enter second number\t"))
num3=int(input("Enter third number\t"))
is_greater(num1,num2,num3)
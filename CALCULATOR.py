num1=int(input("Enter number 1\t:"))
oper=input("Enter operation\t:")
num2=int(input("Enter number 2\t:"))
if oper=='+':
    print(num1+num2)
elif oper=="-":
    print(num1-num2)
elif oper=="*":
    print(num1*num2)
elif oper=="/":
    print(format(num1/num2,'.2f'))
else:
    print("You enter Invaid operator\n")
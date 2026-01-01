#Finding greatest number from 4 number's
num1=int(input("Enter number 1\t\t"))
num2=int(input("Enter number 2\t\t"))
num3=int(input("Enter number 3\t\t"))
num4=int(input("Enter number 4\t\t"))
if num1>num2 and num1>num3 and num1>num4:
    print("Number 1  [",num1,"]  is greater number")
elif num2>num1 and num2>num3 and num2>num4:
    print("Number 2  [",num2,"]  is greater number")
elif num3>num2 and num3>num1 and num3>num4:
    print("Number 3  [",num3,"]  is greater number")
elif num4>num2 and num4>num1 and num4>num3:
    print("Number 4  [",num4,"]  is greater number")
else:
    print("All numbers are equal")
# Checking is student is passed  or failed
sub1=int(input("Enter subject marks 1\t\t"))
sub2=int(input("Enter subject marks 2\t\t"))
sub3=int(input("Enter subject marks 3\t\t"))
if (sub1 and sub2 and sub3)>=33:
    percent=(sub1+sub2+sub3)/3
    if percent>=40.0:
        print("congratulation\nYou passed your exam\nYou got ["+str(format(percent,'.2f'))+"%]")
    else :
        print("You fail Your exam\n you got ["+str(format(percent,'.2f'))+"%]")
else:
    percent=(sub1+sub2+sub3)/3
    print("You fail Your exam\n you got ["+str(format(percent,'.2f'))+"%]")
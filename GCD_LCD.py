#Greatest integers number
num1=int(input("Enter number 1\t:"))
num2=int(input("Enter number 2\t:"))
gcd=1
if(num1>num2):
    for i in range(1,num2):
        if num1%i==0 and num2%i==0:
            gcd*=i
else:
    for i in range(1,num1):
        if num1%i==0 and num2%i==0:
            gcd*=i
lcd=int((num1*num2)/gcd)
print(f"GCD of Two number {num1} and {num2} is {gcd}")
print(f"LCD of Two number {num1} and {num2} is {lcd}")
# CORRECT WAY TO REDUCE TIME COMPLEXITY
num1=int(input("Enter Number 1\t:"))
num2=int(input("Enter Number 2\t:"))
import operator
max,min=max(num1,num2),min(num1,num2)
while min!=0:
    rem=max%min
    max=min
    min=rem
print(max)    
num1=int(input("Enter Number 1\t:"))
num2=int(input("Enter Number 2\t:"))
hcf=1
for i in range(1,min(num1,num2)+1):
    if(num1%i==0 and num2%i==0):
        hcf=i
print(hcf)

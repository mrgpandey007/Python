num=int(input("Enter Number\t:"))
sum=0
for i in range (1,num):
    if issubclass(i**0.5,int):
        sum+=i
        if sum==num:
            print(f"{num} is a sum of perfect number")
            break
else:
    print(f"{num} is not a sum of perfect number ")
num=int(input("Enter Number\t:"))
if (num**0.5-int(num**0.5))==0:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
num=int(input("Enter any number\t"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
    if count>2:
        print(num,"is not a prime number")
if count==2:
    print(num,"is prime a number \n")
num=int(input("Enter any number\t:"))
count=0
for i in range(1,num):
    if num%i==0:
        count+=1
    if count>2:
        print(f"{num} is not prime number\n")
        break
if count==2:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")
#prime number up to N number
num=int(input("Enter Number\t:"))
for i in range(1,num+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
            if count>2:
                break
    if count==2:
        print(i,end=" ")

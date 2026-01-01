num=int(input("Enter Number\t:"))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
        if count>2:
            print(i,": is not a prime number")
            break
if count==2:
    print(i,": is a prime number")
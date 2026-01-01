'''
num=int(input('Enter Number\t:'))
p=c=0
while num!=-1:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
        if count>2:
            c+=1
            break
    if count==2:
        p+=1
    num=int(input("Enter Number\t:"))
print("Composite Number's ",c)
print("Prime number's ",p)'''
for i in range(1,11):
    print(f"1/{i} = {format(float(1/i),'.3f')}")
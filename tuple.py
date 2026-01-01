t1=(1,2,3,4,5,6,7)
l1=[10,20,30,40,50,60,70]
l2=[100,200,300,400,500,600,700]
num=int(input("Enter Number\t:"))

for i in range(2,num):
    if num%i==0: 
        print("no")
        break
else:
    print("Yes")
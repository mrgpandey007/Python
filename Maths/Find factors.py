num=int(input("Enter Number\t:"))
print(f"Factor's of {num}\t:")
for i in range(1,num+1):
    if num%i==0:
        print(i,end="\t")
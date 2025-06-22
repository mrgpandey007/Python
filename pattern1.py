'''
#star pattern
for i in range(1,6):
    for j in range(1,i+1):
        if j==i:
            print("*")
        else:
            print("*",end="")

#internal try by me 

for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    if i==1:
        print("\n")
    for a in range(1,i):
        if a==i-1:
            print("*")
        else:
            print("*",end="")

#pendulum program
for i in range(0,5):
    print(" "*(5-i-1),end="")
    print("*"*(2*i+1))

#middle element have space
n=int(input("Enter any number\t"))
for i in range(n):
    for j in range(n):
        if i==int(n/2) and j==int(n/2):
            print(" ",end="")
        else:
            print("*",end="")
    print("\n",end="")'''
def pattern(num):
    if num==0:
        exit()
    print("*"*num)
    pattern(num-1)
num=int(input("Enter any number"))
pattern(num)
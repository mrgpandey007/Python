'''num=int(input("Enter any number\t"))
print("NORMAL TABLE\t\tREVERSE TABLE")
for i in range(1,11):
    print(num,"x",i,"=",num*i,end="\t\t")
    print(num,"x",11-i,"=",num*(11-i))

#using function
def table(num):
    print("NORMAL TABLE\t\tREVERSE TABLE")
    for i in range(1,11):
        print(num,"x",i,"=",num*i,end="\t\t")
        print(num,"x",11-i,"=",num*(11-i))
num=int(input("Enter any number \t "))
table(num)'''
num=int(input("Enter any number\t: "))
list=[f"{num}x{i+1}={num*(i+1)}" for i in  range(10)]
with open("tablefile.py") as f:
    for i in range(10):
        f.write(str(list[i]))
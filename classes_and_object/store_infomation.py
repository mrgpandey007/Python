class Employee:
    company="microsoft"
    def __init__(self,name,salary,city):
        self.name=name
        self.salary=salary
        self.city=city
    def getdetail(self):
        print(f"\nname is {self.name}\nsalary is {self.salary}\ncity is {self.city}")
e1=Employee("gaurav",100000,"dehradun")
'''def prime_series(n):
    print(f"Prime Number\t:",end="")
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end="\t")
num=int(input("Enter Number\t:"))
prime_series(num)'''
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

def swap(x,y):
    temp =x
    x = y
    y=temp# Driver
x = 2
y=3
swap(x, y)
print(x)
print(y)(dict.keys())


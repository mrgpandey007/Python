def display_list(name):
    for i in range(len(list)):
        print(list[i],sep=",",end=",")
#finding factorial of n number
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
def sub(num1,num2):
    return num1-num2

def is_equal(a,b):
    if a>b:
        print(f"{a} is greater number")
    else:
        print(f"{b} is greater number")

def swap(a,b):
    a,b=b,a
    print(f"After Swaping\nNumber1\t{a}\nNumber2\t{b}")

def full_name(f,l):
    print(f,l)

def aveg(*num):
    sum=0
    for i in num:
        sum+=i
    return sum

#Checking even or old number
def even_or_old(n):
    if n%2==0:    #checking for even number 
        return 1
    else:         #if a number is not even it should we old number 
        return 0
#Coverting hours into minute
def con_mtos(h):
    return h*60
'''
hour=int(input("Enter Hours\t:"))
minute=con_mtos(hour)
print(minute)'''
'''
num=int(input("Enter Number\t:"))
flag=even_or_old(num)
if flag==1:
    print(f"{num} is an even number")
else:
    print(f"{num} is an old number")'''

def fact(n):
    if n==(1 or 0):
        return 1
    return n*fact(n-1)

# WAP to use string documentation and use variable length arguments
def add(*a):
    """this is a adding of a number
    this will diplay addition number"""
    sum=0
    for i in a:
        sum+=i
    return sum

#finding gcd of two number
def gcd(a,b):
    rem=a%b
    if rem==0:
        return b
    else:
        return gcd(b,rem)

def ex(x,y):
    if y==1:
        return x
    else:
        return x*ex(x,y-1)

#Findind febbonics series
def fabbo(n):
    if n<=2:
        return 1
    else:
        return fabbo(n-1)+fabbo(n-2)



















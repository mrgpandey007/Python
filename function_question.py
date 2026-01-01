#printing name with hello
def hello(name):
    print("Hello "+name)

#printing the divisiblity of number n by m 
def display_divisible(m,n):
    for i in range(1,n+1):
        if(i%m==0):
            print(i)

#Checking is three number entered by user is sorted or not 
def issort(num1,num2,num3):
    if num1>num2>num3 or num3>num2>num1:
        print(True)
    else:
        print(False)

#Use documentation in function and S,M,D,U
def printStatus():
    """You are separed"""
    status_code=input("Enter Status\t:")
    if status_code=='S':
        print("Separated")
    elif status_code=="M":
        """you are married"""
        print("Married")
    elif status_code=="D":
        """you have divorced
        you are not good one """
        print("divorced")
    elif status_code=="U":
        """YOU are unmarried"""
        print("Unmarried")
    else:
        """you have entered invaild character try again"""
        print("INVAILD CHARACTER")

#trying documentation 
def greet():
    """Hello every programmer
    how your life going on
    I hope you are enjoying with error's"""
    print("Hello Coder!!!")

#Finding Binomial Coefficient Using Shortcut
def bino_coef(m,x):
    if x==0 or m==0:
        return 1
    else:
        return bino_coef(m,x-1)*((m-x+1)/x)

#Finding Binomial Coefficient Using Shortcut
def fact(num):
    if num==(1 or 0):
        return 1
    return num*fact(num-1)

def b(m,x):
    m_fact=fact(m)
    x_fact=fact(x)
    m_x_fact=fact(m-x)
    print("Coefficient of Binomial Expression is",int(m_fact/(x_fact*m_x_fact)))

#Simple pattern printing using function
def pattern():
    print("********")
    for i in range(3):
        print("!     !")
    print("********")

#Converting celsius into fehrenheit
def c_f(c):
    return 1.8*c+32
#c=int(input("Enter Celsius\t:"))
#print("Fehrenheit\t:"+str(format(c_f(c),'.2f'))+"`F")

#Fabbonic series without using recursion
def Fabbonic(num):
    fab1,fab2=0,1
    for i in range(1,num+1):
        fab,fab1=fab1,fab2
        fab2=fab+fab2
        print(fab)

#Fabbonic series with using recursion
def fabbo(num):
    if num==1:
        return 0
    elif num==2:
        return 1
    return fabbo(num-1)+fabbo(num-2)
'''for i in range(1,9):
    if i==1:
        print(0,end=" ")
    else:
        print(fabbo(i),end=" ")'''

#Finding EXPONENTIAL with function 
def expf(x,y):
    return x**y

#Finding EXPONENTIAL with REcursion function 
def exprf(x,y):
    if y==0:
        return 1
    elif y==1:
        return x
    return x*exprf(x,y-1)

#Reverse a string With help Of Function
def rev(str):
    for i in range(1,len(str)+1):
        print(str[-i],end="")

#Reverse a string with the help of recursion function 
def rev(str):
    if len(str)==0:
        return str
    return rev(str[1:])+str[0]

#fInding Componend interest
def ci(p,r,t):
    return p*((1+r)**t-1)

#Finding the value of power x
def findpow(num,x):
    for i in range(1,num):
        if x**i==num:
            return i
        if x**(-i)==num:
            return i
    else:
      return "Power not exist"

#Find the hypotenuse of the triangle
def findhypo(p,h):
    return int((p**2+h**2)**.5)

#Swapping Number
def swap():
    global a,b
    a,b=b,a
    print(f"a={a}\nb={b}")

#COncentrenating two string
def concen(str1,str2,newstr):
    if len(str1)==0:
        return newstr
    newstr+=str1[0]+str2[0]
    return concen(str1[1:],str2[1:],newstr)

#Time taken  to execute a program 
'''import time 
start_time=time.time()
for i in range(10000):
    if i==1283812:
        print(i)
end_time=time.time()
uses_time=start_time-end_time
print(f"Time taken by the program is {(format(uses_time,'.8f'))}")'''

#Write a function to return absolute value of the number
def absolute(num):
    return abs(num)

#WAP o use lambda function to multiply two number
'''x=int(input("Enter Number\t:"))
a=lambda x: x*x
b=lambda a,x: a*x
print(b(a(x),x))'''

#WAP to find number is prime or not
def is_prime(num):
    if num==0 or num==1 :
        return 0
    else:
        for i in range(2,num):
            if num%i==0:
                return 0
        else:
            return 1

#display mouthname
import calendar
def display_month(n):
    return calendar.month_name[n]

# Swapping testing
def swap(x,y):
    temp=x
    x=y
    y=t

#armstrong Number
def armstrong(num):
    num1=num
    sum=0
    while num>0:
        rem=num%10
        sum+=rem**3
        num//=10
    if sum==num1:
        print("Number is armstrong")
    else:
        print("Number is not armstrong") 
def sum(list):
    sum=0
    for i in list: 
        sum+=i
    return sum
list=[]
size=int(input("Enter Elements to be inserted in list\t:"))
for i in range(size):
    print("Enter Element",i+1,": ",end=" ")
    data=int(input())
    list.append(data)
sum=sum(list)
print("Sum of list elements is ",sum)

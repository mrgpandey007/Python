'''list=[10,20,30,40,50,60,70,80,90]
even=(filter(lambda x: x%4==0,list))
s="s"
list=[1,2]
t=("Good")
a,b=list
t1=1,1.2,"you",True
t2=t1,(1,2,3,4)
t=("Good Morning")
print(t.index("M"))
print(t.index("n",5))
print(t.index("r",4,8))'''
def print_(a,b):
    print(f"A={a}")
    print(f"B={b}")
def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print(f"A={a}")
    print(f"B={b}")
#Write a program to demostate class and object
class Student:
    schoolname="ABC"
s1=Student()
s1.schoolname="XYZ"
print(f"School Name of 1st student is ",s1.schoolname)
s2.Student()
s2.schoolname="Pata nahi"
print(f"School Name of 2nd student is ",s2.schoolname)

#Write a program to demostate constrator
class Person:
    totalperson=0
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        Person.totalperson+=1
p1=Person("ABC",90,34324)
p2=Person("XYZ",20,22413)
print("Totol person=",Person.totalperson)

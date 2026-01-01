class Calculator:
    @staticmethod
    def greet():
        print("HELLO GAUTAM PANDEY SIR JI ")
    def __init__(self,num1):
        self.num1=num1
        print(f"Square of {self.num1}is \t:{self.num1**2}\nCubes of {self.num1}is \t:{self.num1**3}\nSquareroot of the {self.num1}is \t:{self.num1**0.5}")
Calculator.greet()
num1=int(input("Enter any number\t"))
Calculator(num1)
class RailwayInfo:
    def __init__(self,name,age,ph,lunch):
        self.name=name
        self.age=age
        self.ph=ph
        self.lunch=lunch
    def getinfo(self):
        print(f"Your train seat booked suceesfully\nTiming of train\nfrom dehradun\t\tto mumbai\n10:30AM\t\t\t2:30PM\n10/FEB/2024\t\t13/FEB/2024\nNAME\t\t: {self.name}\nAge\t\t:{self.age}\nphone number\t:{self.ph}\nLUNCH\t\t{self.lunch}\nAll the best for your greatfull trip")
name=input("Enter your name\t")
age =input("Enter your age \t")
ph=input("Enter your phone number\t")
lunch=input("Enter your lunch\t")
train=RailwayInfo(name,age,ph,lunch)
train.getinfo()
import random
while 1:
    a=random.randint(1,20)
    b=int(input("Guess any number\t:"))
    if(a>b):
        print(a,"Please Guess small number\n")
    elif b>a:
        print(a,"please select large number\n")
    else:
        print("You guess right number",a)
        exit()
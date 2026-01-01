class Operation:
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def mul(self):
        return self.val1*self.val2
    @staticmethod
    def multiply(val1,val2):
        if(print("The Multiplication is  ",(val1*val2))):
            pass 
        else:
            print("Only integer number of multiplication is allow here \nThank you for using this class ")
class Empolyee_bmi:
    total_person=0
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
        Empolyee_bmi.total_person+=1
    def check_bmi(self):
        bmi=self.weight/self.height**2
        if (bmi<18):
            print(f"{self.name} is Underweight Condition")
        elif bmi>=18 and bmi<=24:
            print(f"{self.name} is healthy condition")
        elif bmi>24 and bmi<=30:
            print(f"{self.name} is overweight condition")
        elif bmi>30 and bmi <40:
            print(f"{self.name} is Obese condition")
        else:
            print(f"{self.name} is extremly obese condition")
obj=Empolyee_bmi("Rahul",70,1.67)
obj.check_bmi()
obj=Empolyee_bmi("Rohit",75,1.65)
obj.check_bmi()
obj=Empolyee_bmi("gulo",90,1.45)
obj.check_bmi()
obj=Empolyee_bmi("aditya",50,1.50)
obj.check_bmi()
print(f"The Total Number of Employee is",obj.total_person)
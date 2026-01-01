class sum:
    def s(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(f"The sum of two number is{self.num1+self.num2}")
num1=int(input("Enter any number 1"))
num2=int(input("Enter any number 2"))
number=sum()
number.s(num1,num2)
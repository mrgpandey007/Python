class University:
    def __init__(self,name,age,dob,adress,department):
        self.name=name
        self.age=age
        self.dob=dob
        self.adress=adress
        self.department=department
    def getdetail(self):
        print(f"Name\t:{self.name}")
        print(f"age\t:{self.age}")
        print(f"DOB\t:{self.dob}")
        print(f"Address\t:{self.adress}")
        print(f"Department\t:{self.department}")
class Student(University):
    def __init__(self,name,age,dob,adress,department,fee,adminsion_no):
        super().__init__(name,age,dob,adress,department)
        self.adminsion_no=adminsion_no
        self.fee=fee
    def getdetail(self):
        super().getdetail()
        print(f"Fees={self.fee}")
        print(f"Adminsion Number\t:{self.adminsion_no}")
s1=Student("gautam",19,"31-08-1978","India","B.Tech CSE",200000,"25BTCSEAI082")
s1.getdetail()

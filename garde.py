#FINDING GRADE OF STUDENT 
percent=int(input("Enter Your percentage\t\t"))
if percent>=90:
    print("Grade->O")
elif percent>=80:
    print("Grade->A")
elif percent>=70:
    print("Grade->B")
elif percent>=60:
    print("Grade->C")
elif percent>=50:
    print("Grade->D")
elif percent>=33:
    print("Grade->E")
else:
    print("Fail")
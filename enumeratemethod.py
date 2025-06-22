num=int(input("Enter any number \t: "))
list=[f"{num}x{i+1}={num*(i+1)}" for i in range(10)]
print(list)
try:
    a=int(input("Enter any number"))
    print(f"The reciporcal of {a} is {1/a}")
except ZeroDivisionError as e:
    print(f"reciporcal of {num} is Infinity")
finally:
    print("Thank for using my code")

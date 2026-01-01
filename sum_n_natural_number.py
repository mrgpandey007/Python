#factorial of n number
num=int(input("Enter any number\t"))
fact=1
for i in range(1,num+1):
    fact*=i
print("Factorial of",num,"number is\t",fact)

#Using recurive function su of n natural number 

def sum_n(num):
    if num==1:
        return 1
    else:
        return num+sum_n(num-1)
num=int(input('Enter any number \t:'))
print("Sum of",num,"is \t",sum_n(num))

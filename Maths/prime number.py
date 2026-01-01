# check whether a number is prime or composite number
def isprime(n):
    if n<2:
        return -1
    for i in range(2,n):
        if num%i==0:
            return 1
    else:
        return 0
num=int(input("Enter Number\t:"))
if isprime(num)==0:
    print(f"{num} is a prime number")
elif isprime(num)==1:
    print(f"{num} is a composite number")
else:
    print(f"{num} is not a prime number")
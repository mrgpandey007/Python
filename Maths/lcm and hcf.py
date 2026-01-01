def hcf(a,b):
    h=0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            h=i
    return h
def lcm(a,b):
    for i in range(max(a,b),a*b+1):
        if i%a==0 and i%b==0:
            return i
num1=int(input("Enter Number 1\t:"))
num2=int(input("Enter Number 2\t:"))
print(f"HCF of {num1} and {num2}\t:{hcf(num1,num2)}")
print(f"LCM of {num1} and {num2}\t:{lcm(num1,num2)}")
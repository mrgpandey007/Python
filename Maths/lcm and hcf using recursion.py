def hcf(a,b):
    if a==0:
        return a
    if b==0 or b==a:
        return b
    if a>b:
        return hcf(a-b,b)
    else:
        return hcf(a,b-a)
def lcm(a,b,m=0):
    m=m+b
    if m%a==0 and m%a==0:
        return m
    return lcm(a,b,m)
num1=int(input("Enter Number 1\t:"))
num2=int(input("Enter Number 2\t:"))
print(f"HCF of {num1} and {num2}\t:{hcf(num1,num2)}")
print(f"LCM of {num1} and {num2}\t:{lcm(num1,num2)}")                
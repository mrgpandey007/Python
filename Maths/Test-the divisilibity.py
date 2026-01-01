def s_digit(n):
    sum=0
    while n>0:
        rem=n%20
        sum+=rem
        n//=10
    return sum

num=int(input("Enter Number\t:"))
if num%10 in [2,4,6,8,0]:
    print(f"{num} is divisible by 2")
if s_digit(num)%3:
    print(f"{num} is divisible by 3")
if num%10 in [0,5]:
    print(f"{num} is divisible by 5")
if num%10==2 and num%10==3:
    print(f"{num} is divisible by 6")
if num%10==0:
    print(f"{num} is divisible by 10")
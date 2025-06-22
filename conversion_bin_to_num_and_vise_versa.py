#Converting decimal number into binary number
num=int(input("Enter Number\t:"))
bin=i=0
while(num>0):
    rem=num%2
    bin+=rem*(10**i)
    num//=2
    i+=1
print("Binary Number is \t:",bin)
#Converting binary number into decimal number
bin=int(input("Enter binary \t:"))
num=i=0
while(bin>0):
    if bin%2!=0:
        num+=(2**i)
    bin//=10
    i+=1
print("Decimal NUmber is \t:",num)
#Converting decimal number into binary number
num=int(input("Enter Number\t:"))
oct=i=0
while(num>0):
    rem=num%8
    oct+=rem*(10**i)
    num//=8
    i+=1
print("octal Number is \t:",oct)
#Converting decimal number into hexadeciml number
num=int(input("Enter Number\t:"))
hex=i=0
while(num>0):
    rem=num%16
    hex+=rem*(10**i)
    num//=16
    i+=1
print("Hexadecimal Number is \t:",hex)
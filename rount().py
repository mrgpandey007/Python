year=int(input("Enter Year\t:"))
if year%4==0 and year%100!=0:
    print(f"{year} is a leaf Year ")
elif year%400==0 and year%100==0:
    print(f"{year} is\
         a leaf Year ")
else:
    print(f"{year} is not a leaf Year ")
name1=input("Enter partner name 1\t:")
name2=input("Enter partner name 2\t:")
true,love="true","love"
t=l=0
for i in true:
    t+=name1.lower().count(i)
    l+=name2.lower().count(i) 
for i in love:
    t+=name1.lower().count(i)
    l+=name2.lower().count(i)
print(f"You and Your partner's love percentage is {str(t)+str(l)}%")

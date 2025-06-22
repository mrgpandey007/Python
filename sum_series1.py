# series 1
'''n=int(input("Enter Number\t:"))
sum=0
for i in range(1,n+1): sum+=(1/i)
print(format(sum,'.2f'))
# series 2
n=int(input("Enter Number\t:"))
sum=0
for i in range(1,n+1): sum+=(1/(i**2))
print(format(sum,'.2f'))
# series 3
n=int(input("Enter Number\t:"))
sum=0
for i in range(1,n+1): sum+=(i/(i+1))
print(format(sum,'.2f'))
# series 4
n=int(input("Enter Number\t:"))
sum=0
for i in range(1,n+1): sum+=((i**i)/i)
print(format(sum,'.2f'))
# series 5
n=int(input("Enter Number\t:"))
sum=0
for i in range(1,n+1,): sum+=(i**3)
print(format(sum,'.2f'))
#series 6
n=int(input("Enter Number\t:"))
sum=0
for i in range(1,n+1): 
    if i%2==0:
        sum+=i**2
print(sum)'''
ini_invt=int(input("Enter investment\t:"))
roi=float(input("Enter Rate of Interest\t:"))
years=int(input("Enter years\t:"))
print("**************************************")
print("\tYears\t\tinvestment")
fut_invt=ini_invt
for i in range(1,years+1):
    fut_invt*=(1+roi/100)
    print(f"\t{i}\t\t{fut_invt}")
#HOW TO FIND THE PRIME FACTORIZATION OF A COMPOSITE NUMBER
def prime_f(num):
    s=""
    for i in range(2,num):
        while 1:
            if num%i==0:
                s+=(str(i)+"  ")
                num//=i
            else:
                break
    return s
num=int(input("Enter Number\t:"))
print(f"Factorisation of {num}\t:{prime_f(num)}")
num=int(input("Enter any number\t: "))
list=[f"{num}x{i+1}={num*(i+1)}" for i in  range(10)]
with open("tablefile.txt",'w') as f:
    for i in range(10):
        f.write(str(list[i])+"\n")
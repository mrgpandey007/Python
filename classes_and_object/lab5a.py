str1=input("Enter a string")
dict={}
k=1
for i in str1:
    d={k:i}
    k+=1
    dict.update(d)
print(dict)
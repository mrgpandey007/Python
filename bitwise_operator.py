list=[10,20,30,40,50,"han bhai kya chal raha hai yei sab"]
list2=[60,70,80,90,100]
list.extend(list2)
dict={1:"one",2:"two",3:"Three",4:"four"}
dict={}
n=int(input("Enter N number of Student\t:"))
for i in range(n):
    dict[input("Enter Name\t:")]=[int(input("Enter Registration Number\t:")),int(input("Enter Marks\t:"))]
print(dict)
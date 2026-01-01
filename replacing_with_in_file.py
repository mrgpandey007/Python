'''with open("poems.txt")as f:
    data=f.read()
with open("poems.txt",'w')as f:
    data=data.replace('Twinkle','#######')
    f.write(data)
    print("Data Updated suceessfully")'''
#using list of words
list=["Twinkle",'night','diamond']
with open("poems.txt") as f:
    data=f.read()
with open("poems.txt",'w') as f:
    for i in list:
        data=data.replace(i,'gautam')
    f.write(data)
    print("upadated sucessfully")
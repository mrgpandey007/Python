str1=""
for i in range(1,11):
    for j in range(2,21):
        str1+=str(j)+str("x")+str(i)+str("=")+str(j*i)+str('\t')
    str1+=str("\n")
with open("13_year_old",'w')as f:
    f.write(str1)
    print("Table added suceesfully")
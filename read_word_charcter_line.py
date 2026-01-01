with open("poems.txt",'r') as f:
    data=f.read()
    length=len(data)
    print("NUMBER OF CHARCTER IS ",length)
    count=data.count("\n")+1
    print("NUMER OF LINES IN THE FILE IS ",count)
    count=data.count(" ")
    print("NUMER OF words IN THE FILE IS ",count+1)
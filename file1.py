with open('poems.txt','r') as f:
    data=f.read()
    if 'Gautam'in data:
        print('Yes the word Twinkle exist in the file of poem')
    else:
        print("not exist")
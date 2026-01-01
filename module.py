def pow(x,y=3):
    r=1
    for i in range(y):
        r*=x
    return r

def even(x):
        if x%2==0:
                return True
        else:
                return old(x-1)
def old(x):
        return even(x)
print(even(67))
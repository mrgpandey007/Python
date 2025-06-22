def sq(x): return x*x
def add(x,y): return x+y
list=[]
list=[i for i in range(1,11)]

l=list(filter(sq,range(1,11)))
import functools
sum=functools.reduce(add,list)
print(sum)
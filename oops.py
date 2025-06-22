def funct1(i):
    return i/0
def funct2():
    raise Exception("Raining Exceptation...")
def funct3():
    try:
        funct1(5)
    except Exception as e:
        print(e)
        raise
    try:
        funct2()
    except Exception as e:
        print(e)
try:
    raise TypeError('int Excepted')
except TypeError:
    raise
'''def c_f(celsius):
    return 1.8*celsius+32
celsius=int(input("Enter celsius\t"))
print("Fehrenheit is \t",c_f(celsius))
while(1):
    g=int(input("Enter Gram\t:"))
    print(f"{g}g-->{format(g/1000,'.3f')}Kg")
    m=int(input("Enter Meter\t:"))
    print(f"{m}m-->{m*100}cm")
import unicodeit
for i in range(1,9):
    print(f"{unicodeit.replace('2^')}-->{2**i}")'''
hourly=int(input("Enter Hourly wage\t:"))
r_hour=int(input('Enter Total Regular\t:'))
v_hour=int(input("Enter Totak Overtime Hours\t:"))
print(f"Your Total Weekly Pay-->{(r_hour*hourly+v_hour*hourly*1.5)*7}")

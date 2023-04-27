import math
a = float(input())
b = float(input())
c = float(input())

delta = (b**2)-(4*a*c)

if delta >= 0:
    x1 = ((-b)+(math.sqrt(delta)))/(2*a)
    print(f'{x1:.2f}')
    if delta > 0:
        x2 = ((-b)-(math.sqrt(delta)))/(2*a)
        print(f'{x2:.2f}')
else:
    print("nao ha raiz real")
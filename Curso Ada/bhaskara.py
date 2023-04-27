import math
a = float(input())
b = float(input())
c = float(input())

delta = (b**2)-(4*a*c)
print(delta)

x1 = ((-b) + math.sqrt(delta))/(2*a)
print(x1)

x2 = ((-b) - math.sqrt(delta))/(2*a)
print(x2)
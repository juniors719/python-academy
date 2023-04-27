import math

xa = float(input())
ya = float(input())
xb = float(input())
yb = float(input())

dist = math.sqrt(((xb-xa)**2)+((yb-ya)**2))

print(f'{dist:.2f}')
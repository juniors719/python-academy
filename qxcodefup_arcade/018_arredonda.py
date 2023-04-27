import math
op = input()
numero = float(input())

if op == 'r':
    print(round(numero))
if op == 'f':
    print(math.floor(numero))
if op == 'c':
    print(math.ceil(numero))
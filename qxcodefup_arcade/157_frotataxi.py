pA = float(input())
pG = float(input())
rA = float(input())
rG = float(input())

cA = rA/pA
cG = rG/pG

if cA > cG:
    print("A")
else:
    print("G")
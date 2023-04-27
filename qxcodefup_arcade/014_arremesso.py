a = int(input())
b = int(input())
c = int(input())

if a == b and a == c and b == c:
    cont = 3
elif a == b or a == c or b == c:
    cont = 2
else:
    cont = 0

print(cont)
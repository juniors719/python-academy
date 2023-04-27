n1 = int(input())
n2 = int(input())
op = input()

if op == '+':
    res = n1+n2
elif op == '-':
    res = n1-n2
elif op == '*':
    res = n1*n2
else:
    res = n1//n2

print(res)
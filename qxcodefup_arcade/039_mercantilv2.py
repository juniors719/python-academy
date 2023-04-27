jog1 = float(input())
jog2 = input()
valor_real = float(input())

if jog1 == valor_real:
    vencedor = 1
else:
    if jog2 == 'm':
        if jog1 > valor_real:
            vencedor = 0
        else:
            vencedor = 1
    if jog2 == 'M':
        if jog1 < valor_real:
            vencedor = 0
        else:
            vencedor = 1

if vencedor:
    print("primeiro")
else:
    print("segundo")
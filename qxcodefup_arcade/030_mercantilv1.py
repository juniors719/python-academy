valor_real = float(input())
primeiro = float(input())
segundo = float(input())

diferenca1 = abs(valor_real - primeiro)
diferenca2 = abs(valor_real - segundo)

if diferenca1 > diferenca2:
    print("segundo")
elif diferenca2 > diferenca1:
    print("primeiro")
else:
    print("empate")
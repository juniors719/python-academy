hora = float(input('Digite o valor da sua hora de trabalho: R$ '))
q = int(input('Digite a quantidade de horas trabalhadas: '))

salario_bruto = hora * q 

if salario_bruto <= 900:
    pIR = 0
elif salario_bruto <= 1500:
    pIR = 5
elif salario_bruto <= 2500:
    pIR = 10
else:
    pIR = 20
ir = salario_bruto * (pIR/100)
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11
total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto (R$ {hora:.2f} * {q}): R$ {salario_bruto:.2f}")
print(f"(-) IR ({pIR}%): R$ {ir:.2f}")
print(f"(-) INSS (10%): R$ {inss:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
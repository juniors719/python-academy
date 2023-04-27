# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

salH = float(input('Digite o quanto você ganha por hora: '))
horas = int(input('Digite a quantidade de horas trabalhadas no mês: '))

salario = salH * horas

print(f"Salário: R$ {salario:.2f}")

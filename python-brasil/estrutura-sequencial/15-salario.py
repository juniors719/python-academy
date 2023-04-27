# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

salH = float(input('Digite quanto você ganha por hora: '))
horas = int(input('Digite a quantidade de horas trabalhadas: '))

salB = salH * horas # salário bruto

ir = salB * 0.11 # imposto de renda

inss = salB * 0.08 # inss

sind = salB * 0.05 # sindicato

salL = salB - ir - inss - sind # salário líquido

print(f'+ Salário Bruto : R$ {salB:.2f}')
print(f'- IR (11%) : R$ {ir:.2f}')
print(f'- INSS (8%) : R$ {inss:.2f}')
print(f'- Sindicato (5%) : R$ {sind:.2f}')
print(f'= Salário Liquido : R$ {salL:.2f}')

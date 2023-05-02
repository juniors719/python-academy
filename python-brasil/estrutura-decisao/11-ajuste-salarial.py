t = 'ORGANIZAÇÕES TABAJARA'
print(f'{t:*^50}')

salario = float(input('Digite seu salário atual: '))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
elif salario >  1500:
    percentual = 10

aumento = salario * (percentual/100)

print(f'Salário antes do reajuste: R$ {salario:.2f}'.replace('.',','))
print(f'Percentual de reajuste: {percentual}%')
print(f'Valor do aumento: R$ {aumento:.2f}'.replace('.',','))
print(f'Salário após o reajuste: R$ {(salario+aumento):.2f}'.replace('.',','))


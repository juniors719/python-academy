salario = float(input('Digite o valor do seu salário atual: '))
perc = float(input('Digite o percentual de reajuste: '))

salario = salario * (1 + (perc/100))

print(f'Seu novo salário é: R$ {salario:.2f}')
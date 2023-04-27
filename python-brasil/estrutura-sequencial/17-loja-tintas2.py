# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta
# é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

latas = 0
baldes = 0

area = float(input('Digite a área a ser pintada em m²: '))

# 1 litro de tinta = 6 metros quadrados
quantL = area/6

# folga de 10%
quantL *= 1.10

# quantidade de latas de 18 litros
if quantL >= 18:
    latas = int(quantL // 18)
    quantL %= 18 # restante dos litros

    # quantidade de baldes
    if quantL > 0:
        if quantL > 3.6:
            baldes = quantL / 3.6
        else:
            baldes = 1
        baldes = math.ceil(baldes)
else:
    latas = 1


print(f'Área a ser pintada: {area}m²')
print(f'Quantidade de latas: {latas} lata(s)')
print(f'Quantidade de baldes: {baldes} balde(s)')

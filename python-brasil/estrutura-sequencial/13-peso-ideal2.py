# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule 
# seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input('Digite sua altura, em metros: '))

# alternativa a

pesoIdealH = (72.7*h) - 58

# alternativa b

pesoIdealM = (62.1*h) - 44.7

# Saída

print(f'Peso ideal (Homem): {pesoIdealH:.1f}kg')
print(f'Peso ideal (Mulher): {pesoIdealM:.1f}kg')
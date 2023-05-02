n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# Ternário:
# a if condition else b
maior = n1 if (n1 > n2) else n2

print(f'Maior número: {maior}')
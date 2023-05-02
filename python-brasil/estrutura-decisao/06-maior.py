# n = []

# for i in range(3):
#     n.append(int(input(f'Digite o número {i+1}: ')))
# maior = max(n)

n1 = int(input(f'Digite o primeiro número: '))
n2 = int(input(f'Digite o segundo número: '))
n3 = int(input(f'Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print(f'O maior número é: {maior}')
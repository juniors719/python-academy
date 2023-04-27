notas = []
for i in range(4):
    notas.append(float(input(f'Informe a nota {i+1}: ')))

media = sum(notas) / len(notas)

print(f'A média das notas é {media:.2f}')
print(f'A maior nota é {max(notas)}')
print(f'A menor nota é {min(notas)}')
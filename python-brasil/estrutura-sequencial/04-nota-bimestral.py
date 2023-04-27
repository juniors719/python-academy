notas = 0
for i in range(4):
    notas += float(input(f'Digite a nota {i+1}: '))
media = notas/4
print(f"Média: {media:.1f}")
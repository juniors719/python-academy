n1 = float(input('Digite a primeira nota parcial: '))
n2 = float(input('Digite a segunda nota parcial: '))
media = (n1+n2)/2
conceito = ''
if media < 4: conceito = 'E'
elif media < 6: conceito = 'D'
elif media < 7.5: conceito = 'C'
elif media < 9: conceito = 'B'
elif media <= 10: conceito = 'A'
res = 'APROVADO' if conceito == 'A' or conceito == 'B' or conceito == 'C' else 'REPROVADO'
print(f"Média: {media:.1f} | Conceito: {conceito} | {res}")
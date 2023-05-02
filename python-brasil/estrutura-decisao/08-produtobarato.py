p1 = float(input('Digite o preço do primeiro produto: '))
p2 = float(input('Digite o preço do segundo produto: '))
p3 = float(input('Digite o preço do terceiro produto: '))

if p1 < p2 and p1 < p3:
    menor = 'primeiro'
    preco = p1
elif p2 < p1 and p2 < p3:
    menor = 'segundo'
    preco = p2
else:
    menor = 'terceiro'
    preco = p3

print(f'Opte por comprar o {menor} produto, que custa R$ {preco:.2f}')
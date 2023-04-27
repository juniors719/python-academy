v = []
for u in range(15):
    n = input('Digite um número:')
    v.append(n)

b = input('Digite o valor a ser buscado: ')
ind = str(v.index(b))
if ind:
    print('Indice do valor:' + ind)
else:
    print('Valor nao encontrado')
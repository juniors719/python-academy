from random import randint

CAPACIDADE_BALDE = 1000

balde = 0

while balde <= CAPACIDADE_BALDE:
    copo = randint(95, 100)
    print(f'O copo foi enchido até: {copo}ml')
    if copo + balde <= 1000:
        balde += copo
        print(f'QUANTIDADE DE ÁGUA ATUAL NO BALDE: {balde}ml'.capitalize())
    else:
        print("Balde irá transbordar!!!")
        break

print("BALDE CHEIO")
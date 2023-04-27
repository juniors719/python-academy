# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # a) o produto do dobro do primeiro com metade do segundo .
    # b) a soma do triplo do primeiro com o terceiro.
    # c) o terceiro elevado ao cubo.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
nf = float(input('Digite um número real: '))

# alternativa a

res = (2 * n1) + (n2 / 2)
print(f'a) {res}')

# alternativa b

res = (n1 * 3) + nf
print(f'b) {res}')

# alternativa c

res = nf ** 3
print(f'c) {res}')
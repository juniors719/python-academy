def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um número: '))
if par(n):
    print('O número é par')
else:
    print('O número é ímpar')

n = int(input('Digite a quantidade de copos da base: '))
pontos = n-1;
for i in range(1, n+1):
    s = ''
    for p in range(pontos):
        s += '.'
    for j in range(i):
        s += str(n)
        if j != i-1: s += '.'
    for p in range(pontos):
        s += '.'
    print(s)
    pontos -= 1
hora = int(input())
minuto = int(input())
dia = int(input())
mes = int(input())
ano = int(input())

hora %= 24
ano %= 100

print(f'{hora:0>2d}:{minuto:0>2d} {dia:0>2d}/{mes:0>2d}/{ano:0>2d}')
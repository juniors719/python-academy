valor = float(input())
parc = int(input())

juros = (5*(parc-1))/100

valor_parcela = valor / parc
valor_parcela = valor_parcela + (valor_parcela * juros)

valor_total = valor_parcela * parc

print(f'{valor_parcela:.2f}')
print(f'{valor_total:.2f}')
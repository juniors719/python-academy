l1 = []
l2 = []
while True:
    n = int(input("L1 - Digite um numero inteiro(0 sai): "))
    if n == 0:
        break
    else:
        l1.append(n)
while True:
    n = int(input("L2 - Digite um numero inteiro(0 sai): "))
    if n == 0:
        break
    else:
        l2.append(n)

lista_final = l1 + l2;
print(lista_final)

lista_norep = []
for i in lista_final:
    if not i in lista_norep:
        lista_norep.append(i)

print(lista_norep)
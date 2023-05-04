dia = int(input('Digite um número correspondente ao Dia da Semana: '))

dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
if dia > 0 and dia < 8:
    print("Dia da Semana: " + dias[dia-1])
else:
    print("Valor Inválido")

# if dia == 1:
#     diaS = 'Domingo'
# elif dia == 2:
#     diaS = 'Segunda'
# elif dia == 3:
#     diaS = 'Terça'
# elif dia == 4:
#     diaS = 'Quarta'
# elif dia == 5:
#     diaS = 'Quinta'
# elif dia == 6:
#     diaS = 'Sexta'
# elif dia == 2:
#     diaS = 'Sábado'
# else:
#     print("Valor Inválido")
#     exit()

# print("Dia da Semana: " + diaS)

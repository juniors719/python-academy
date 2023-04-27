dia = int(input())
hora = int(input())
minuto = int(input())
trabalhando = False

if dia >= 2 and dia <= 6:
    if (hora >= 8 and hora < 12)or(hora >= 14 and hora < 18):
        trabalhando = True
elif dia == 7:
    if hora >= 8 and hora < 12:
        trabalhando = True
if trabalhando:
    print("SIM")
else:
    print("NAO")

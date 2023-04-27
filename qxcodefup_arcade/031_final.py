n1 = float(input())
n2 = float(input())
nf = float(input())

media = (n1+n2)/2
#print(media)

if media >= 7:
    print("aprovado")
elif media < 7 and media >= 4:
    mediaf = (media + nf)/2
    if mediaf >= 5:
        print("aprovado na final")
    else:
        print("reprovado na final")
else:
    print("reprovado")
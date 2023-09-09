def calc_media_mediana(notas):
    media = sum(notas) / len(notas)
    mediana = 0

    if len(notas) % 2 == 0:
        # número par
        notas_ordenadas = sorted(notas)
        indice_ponto_central_menor = int(len(notas)/2) - 1
        indice_ponto_central_maior = int(len(notas)/2)
        mediana = (notas_ordenadas[indice_ponto_central_menor] + notas_ordenadas[indice_ponto_central_maior]) / 2
    else :
        # número ímpar
        notas_ordenadas = sorted(notas)
        indice_mediana = int(len(notas)/2)
        mediana = notas_ordenadas[indice_mediana]

    return media, mediana


resultado_media, resultado_mediana = calc_media_mediana([5,6,4,5])
print(resultado_media)
print(resultado_mediana)
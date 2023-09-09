def funcao_com_args(arg1, arg2, *args):
    print(f"Arg1: {arg1}")
    print(f"Arg2: {arg2}")
    print(f"*Args: {args}")

def soma(maximo, *numeros):
    resultado = 0
    numeros_somados = []

    for numero in numeros:
        if (resultado + numero) > maximo:
            break

        resultado += numero
        numeros_somados.append(numero)

    return resultado, numeros_somados

resultado, numeros_somados = soma(100, 1, 2, 3, 34, 60, 4, 100)
print(resultado)
print(numeros_somados)
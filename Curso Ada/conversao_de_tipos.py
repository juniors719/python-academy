#   CONVERSÃO DE TIPOS

idade = '26' # str
numero1 = '10' # str
numero2 = '20' # str

print(numero1+numero2) # Concatena os textos

print(idade, type(idade))

idade_inteira = int(idade) # Converte a variável idade em inteiro (Conversão explícita)

print(idade_inteira, type(idade_inteira))

# int()
# str()
# float()
# bool()

altura = float(input("Informe a sua altura: ")) # o input sempre lê como str
print(altura, type(altura))
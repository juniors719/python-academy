import random

numero_sorteado = random.randrange(1,20)

numero_escolhido = int(input("Informe um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
    numero_escolhido = int(input("Você errou... Tente novamente: "))

print("Você acertou!")
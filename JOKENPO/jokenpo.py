from random import randrange

print("*"*56)
title = "PEDRA, PAPEL OU TESOURA!!"
print(f"{title:-^56}")
print("*"*56)
print(">>>> 0 para Pedra || 1 para Papel || 2 para Tesoura <<<<")

options = ["Pedra", "Papel", "Tesoura"]

win = False
rodada = 1
while not win:
    titulo_rodada = f" Rodada {rodada} "
    print(f"{titulo_rodada:_^56}")
    pc = randrange(0,3)
    user = 3
    while user < 0 or user > 2:
        user = int(input("Digite sua opção: "))
        if user < 0 or user > 2:
            print("Digite uma opção válida!!!")

    # Imprime as escolhas
    print("-"*56)
    print(f"> PC escolheu: {options[pc]}")
    print(f"> Você escolheu: {options[user]}")
    print("-"*56)

    # Caso o usuário escolha Pedra
    if user == 0:
        # Se PC escolher Tesoura, usuário ganha
        if pc == 2:
            winner = 1
            win = True
        # Se PC escolher Papel, PC ganha
        elif pc == 1:
            winner = 0
            win = True
        # Senão, o jogo continua
        else:
            print("Empate")
    
    # Caso o usuário escolha Papel
    if user == 1:
        # Se PC escolher Pedra, usuário ganha
        if pc == 0:
            winner = 1
            win = True
        # Se PC escolher Tesoura, PC ganha
        elif pc == 2:
            winner = 0
            win = True
        # Senão, o jogo continua
        else:
            print("Empate")

    # Caso o usuário escolha Tesoura
    if user == 2:
        # Se PC escolher Papel, usuário ganha
        if pc == 1:
            winner = 1
            win = True
        # Se PC escolher Pedra, PC ganha
        elif pc == 0:
            winner = 0
            win = True
        # Senão, o jogo continua
        else:
            print("Empate")
    rodada = rodada + 1

if winner == 0:
    print("Você perdeu! :(")
else:
    print(">>>>> Você ganhou!!! :D <<<<<")
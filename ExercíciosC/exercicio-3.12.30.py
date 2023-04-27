exec = True
casado = 0
viuvo = 0
solteiro = 0
separ = 0
pessoas = 0
idadeV = 0
while exec:
    pessoas+=1
    idade = int(input('Digite sua idade: '))
    ec = input('Digite seu estado civil: ').upper()
    print('-'*50)
    if ec == 'C':
        casado+=1
    elif ec == 'V':
        viuvo+=1
        if idadeV == 0:
            idadeV += idade
        else:
            idadeV = (idadeV + idade)/2
    elif ec == 'S':
        solteiro+=1
    elif ec == 'D':
        separ+=1
    if idade < 0:
        print('Execução finalizada'.upper())
        print('-'*50)
        percS = (separ / pessoas)*100
        exec = False

print(f'Quantidade de pessoas casadas: {casado}')
print(f'Qunatidade de pessoas solteiras: {solteiro}')
print(f'Média de idade das pessoas viúvas: {idadeV}')
print(f'Porcentagem de pessoas separadas: {percS:.2f}%')

    
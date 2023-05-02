letra = input('Digite uma letra: ').lower()
vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais:
    print('vogal')
else:
    print('consoante')
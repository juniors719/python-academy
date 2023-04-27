print('     Strip     '.strip())
# strip() -> Remove os espaços em branco

print('MINUSCULO'.lower())
# lower() -> texto em minúsculo

print('maiusculo'.upper())
# upper() -> texto em minúsculo

print('T,exto, c,o,m vá,ria,s v,í,rgu,las'.replace(',',''))
# replace() -> troca um caractere por outro 

print('Texto para teste para função count'.count('e'))
# count() -> Retorna a contagem do número de ocorrências do parâmetro informado

print('Texto centralizado'.center(50,'*'))
# center() -> Centraliza o texto, usando algum caractere como preenchimento

print('Avião?'.index('ã'))
# index() -> retorna a posição na string da ocorrência do caractere informado

print('o10'.isnumeric())
# isnumeric() -> testa se todos os caracteres da string são numéricos

print('Teste de quebra de string com split'.split(' '))
# split() -> Quebra a string onde tem o caractere especificado, gerando uma lista com todas as substrings
print('NOME;CIDADE;IDADE;PAÍS'.split(';'))

print('este é um título'.title())
# title() -> coloca as inicias de todas as palavras da string em maiúsculo

print('este é um título'.capitalize())
# capitalize() -> coloca somente a primeira letra da string em maiúsculo

print('585'.zfill(8))
# zfill() -> completa com zeros à esquerda, no tamanho especificado no parâmetro


#  ENCADEAMENTO DE FUNÇÕES

print('   Te;x;t;;o    '.strip().replace(';','').center(25, '-').upper())


#  TAMANHO DAS STRINGS

string_extensa = 'Essa é uma string extensa. Como faremos para saber o seu tamanho?'

print(len(string_extensa))




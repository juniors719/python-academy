#   LISTAS ou ARRAYS

#   antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#   com LISTA
notas = [7,9, 9.7, 8.2]

#   Criando Listas
lista = [] # lista vazia
lista = list() # função que cria lista vazia
lista = [24, 'Junior', 3.14, True] # Lista com vários tipos de variáveis
lista_de_listas = [1, [1,2,3]] # Listas de listas

#   Indexação e Slices (fatiamento)
lista = [24, 'Junior', 3.14, True]
print(lista[0]) # Indexação do valor - inicia em 0
print(lista[1])
print(lista[2])
print(lista[3])

#Também dá pra usar números negativos. -1 = último; -2 = penúltimo; etc.

#   Slices (FATIAMENTO)
lista = [10,20,30,40,50]
print(lista[0:3]) # de 0 até 'menor que' 3
print(lista[0:]) # de 0 até o final
print(lista[0:5:2]) # ppula de 2 em 2

# > INTERAÇÕES COM FOR
for elemento in lista:
    print(elemento)
# percorre todos os elementos da lista

print("Comprimento da lista: ", len(lista)) # imprime tamanho da lista

for i in range(len(lista)):
    print(lista[i])
# usando len() para percorrer e imprimir todos os elementos da lista
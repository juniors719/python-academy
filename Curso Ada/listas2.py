#   MÉTODOS DE LISTAS

lista = [1,3,12,8,2]

# > append() - Adicionar no final da lista

print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)


# > insert() - Adiciona no índice que você escolher

lista.insert(2,10) #insert('índice','valor')

print('Depois do insert: ', lista)


# > extend() - Junta duas listas

lista2 = [1, 2, 3]
lista.extend(lista2)

print('Depois do extend: ', lista)


# > pop() - Remove um índice que vc especificar, ou o último se n especificar

lista.pop()
print('Depois do pop sem especificar: ', lista)

lista.pop(0)
print('Depois do pop especificando: ', lista)


# > remove() - Remove um valor específico

lista.remove(3)
print('Depois do remove: ', lista)
# Só remove o primeiro valor que ele encontra


# > count() - Conta valores na lista

print("Quantidade de 2 na lista: ", lista.count(2))


# > index() - 

print("Índice do elemento 12: ", lista.index(12))


# > sort() - Ordena de forma crescente a lista

lista.sort()
print('Depois do sort: ', lista)

# descrescente

lista.sort(reverse=True)
print('Depois do sort reverso: ', lista)




#   FUNÇÕES PARA LISTAS

# > len - Retorna o tamanho da lista

print("Tamanho da lista: ", len(lista))


# > sum - Retorna a soma de todos os elementos da lista

print("Soam de todos os elementos da lista: ", sum(lista))


# > max - Retorna o maior elemento da lista

print("Maior elemento da lista: ", max(lista))


# > min - Retorna o menor elemento da lista

print("Menor elemento da lista: ", min(lista))
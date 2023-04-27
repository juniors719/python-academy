# > DICIONARIOS

# Criando dicionários

dicionario = {} # dicionario vazio
dicionario = dict() # Função para criar dicionario vazio

dicionario = { 'nome' : 'Júnior', 'idade' : 24, 'altura' : 1.65 } # dicionario com valores e keys

print(dicionario['nome']) # Acessando por key


# Adicionando elementos em um dicionário

dicionario['programador'] = True # Adiciona uma key (pq n existia) e o valor

print(dicionario)

dicionario['altura'] = 2 # Adiciona o valor na key já existente

print(dicionario)


# Iterando com dicionários

for i in dicionario:
    print(i) # Imprime a key

for i in dicionario:
    print(i, dicionario[i]) # Imprime a chave e o valor


# Testar a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)
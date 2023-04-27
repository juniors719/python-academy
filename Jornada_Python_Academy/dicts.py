# cadastro = {
#     'id' : 1,
#     'nome' : 'João Carlos da Silva',
#     'filhos' : ['Joana', 'Sarah'],
#     'compras' : [
#         {
#             'id' : 4758,
#             'produto' : 'Notebook Gamer',
#             'preco' : 2597.99
#         }
#     ]
# }

# print(cadastro['compras'][0]['produto'])

# notebook_gamer = cadastro['compras'][0]

# print(f'O usuário {cadastro["nome"]} realizou a seguinte compra: {notebook_gamer["produto"]}')

# altura = cadastro.get('altura', None)
# print(altura)




# computador = {
#     'cpu' : 'Core i7',
#     'ram' : 'DDR4 16GB',
#     'ssd' : 'Samsung Evo 840 256gb',
#     'gpu' : 'RTX 2080 Ti'
# }

# print(f"Computador V1 : {computador}")

# computador['ram'] = 'DDR4 32GB'

# print(f"Computador V2 : {computador}")

# computador['fonte'] = 'Fonte 600W Corsair'

# print(f"Computador V3 : {computador}")

# computador.update({'fonte' : 'Fonte 850W Corsair', 'ssd' : 'Samsung Evo 840 1TB'})

# print(f"Computador V4 : {computador}")




# fila = {
#     'pessoa0' : 'João',
#     'pessoa1' : 'Joana',
#     'pessoa2' : 'Clara',
#     'pessoa3' : 'Ana',
#     'pessoa4' : 'Júlia',
# }

# print(f"Fila inicial: {fila}")

# # del

# del fila['pessoa0']

# print(fila)

# # pop

# valor_retirado = fila.pop('pessoa1')

# print(fila)
# print(valor_retirado)

# # popitem

# fila.popitem() # apaga o último elemento

# print(fila)

# # clear

# fila.clear()

# print(fila)




familia = {
    'pai' : 'José da Silva',
    'mae' : 'Ana Almeida',
    'filho' : 'Cléber da Silva Almeida',
    'filha' : 'Joana da Silva Almeida'
}

print(f"Família : {familia}")

# COPY
# copia um dicionario

copia_familia = familia.copy()
print(f'Cópia: {copia_familia}')

# ITEMS
# Retorna os pares chave: valor em formato de lista

itens = familia.items()
print(f'Itens: {itens}')

for item in itens:
    print(f'\tChave = {item[0]}, e valor = {item[1]}')

# KEYS
# Retorna as chaves em formato de lista

chaves = familia.keys()
print(f'Chaves = {chaves}')

for chave in chaves:
    print(f'Chave = {chave}')

# VALUES
# Retorna todos os valores em formato de lista

valores = familia.values()
print(valores)

for valor in valores:
    print(f'Valores = {valor}')

# SETDEFAULT
# Insere a chave com o valor passado SE a chave não estiver no dicionário
# Retorna o valor da chave SE a chave já estiver no dicionário

familia.setdefault('sobrinho', 'Carlos Silva')

print(familia)

mae = familia.setdefault('mae', 'Dona Florinda')

print(familia)
print(mae)

# FROMKEYS
# Cria um dicionário a partir de uma lista de chaves e um valor

chaves = ['mae', 'pai', 'filho', 'filha']
valor = 0

jogo = dict.fromkeys(chaves, valor)

print(jogo)




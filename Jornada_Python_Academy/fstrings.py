titulo = 'Monitor Gamer'
polegadas = 27
preco = 1299.99

# print(f'Nome do produto: {titulo} \nTamanho: {polegadas} polegadas')

# > Usando print em várias linhas e f strings

print(
    f'Produto: {titulo.upper():-^100}\n'
    f'Tamanho: {polegadas}\n'
    f'Preço: R$ {preco}\n'
)

# * caractere que será completado
# ^ texto centralizado
# 50 tamanho final da string, contando o texto da variável
# < alinhado à esquerda
# > alinhado à direita
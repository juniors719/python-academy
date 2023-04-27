#   FUNÇÕES 

"""
# print() - Imprime uma mensagem
# input() - Retorna um dado informado pelo usuário
# len() - Retorna a quantidade de elementos de uma lista
# max() - Retorna o maior valor de uma lista
"""

# > COMO CRIAR UMA LISTA

# Função inicial

def saudacao():
    print("Seja bem-vindo")
    print("Olá, é um prazer ter você fazendo parte deste curso!")


# Função com parâmetros

def saudacao(nome,curso):
    print(f"Seja bem-vindo {nome}")
    print(f"Olá, é um prazer ter você fazendo parte do curso de {curso}!")

""" saudacao('Júnior','Python') """


# Função com parâmetros default

def saudacao(nome,curso="Python"):
    print(f"Seja bem-vindo {nome}")
    print(f"Olá, é um prazer ter você fazendo parte do curso de {curso}!")

saudacao('Júnior')


# Função com retorno

def soma(n1,n2):
    return n1+n2

# OBS.: return PARA(BREAK) a execução da função

print(soma(1,2))
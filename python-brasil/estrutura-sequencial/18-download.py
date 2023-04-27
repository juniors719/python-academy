# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet 
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = int(input('Digite o tamanho do arquivo em MB: '))
veloc_internet = int(input('Digite a velocidade do link em Mbps: '))

# Converter a velocidade para MB/s
vel_mb = veloc_internet / 8

# Calcular o tempo aproximado em minutos
# Perceba que o tempo está em segundos
tempo = int((tamanho_arquivo / vel_mb) / 60)

print(f'O tempo aproximado necessário é de {tempo} minutos')
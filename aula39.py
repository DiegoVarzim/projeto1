"""
Iterando strings com while
"""

#       01234567891011
nome = 'Diego Varzim'  # Iteráveis
#       11109876543210

'''
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[11])
'''


indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

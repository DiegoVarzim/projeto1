""" while/else  - enquato/outro
"""

string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]


    if letra == ' ':
        break                  # parar o código quando encontrar um espaço em branco

    print(letra)
    i += 1

else:
    print('Não encontrei um espaço na string')
print('Fora do while.')


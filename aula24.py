# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# D i e g o
# 6-5-4-3-2-1

# nome = 'Diego'
# print(nome[2])
# print(nome [-3])
'''print('e'in nome)
print('z' in nome)
print('1' in nome)
print('zero' in nome)
print(10 * '-')
print('ego' in nome)
print('ego' not in nome)'''

nome = input('Digita seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')




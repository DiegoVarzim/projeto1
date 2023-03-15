"""
Calculadora com while (enquanto/looping)

.lower - converte tudo que for minúsculo para maiúsculo.

"""

while True:
    print('')
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

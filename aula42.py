frase = 'aaaooo'


# .count - conta quantas vezes uma palavra apareceu na frase.

# CASES
# .upper - letras maiúsculas
# .lower - letras minúsculas
# i - iteração (iterável)
# len()  - obter o número de itens em um determinado objeto, string, array, listas, entre outros.

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x '
)

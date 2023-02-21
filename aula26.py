'''
Formatação básica de strings
s - string
d - int (integer)
f - float
.<número de dígitos>f
x ou x - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda 
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a       __repr__ __str __
'''


variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:$^10}.')
print(f'{1000.5859586968640494:.1f}')
print(f'{1000.5859586968640494:.5f}')
print(f'{1000.5859586968640494:,.5f}')
print(f'{10000.5859586968640494:,.5f}')
print(f'{-1000.5859586968640494:.1f}')
print(f'{1000.5859586968640494:+.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')







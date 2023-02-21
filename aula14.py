a = 'AAAAA'
b = 'BBBBB'
c = 1.1
d = 2.0
string = 'a={nome1} b={nome2} c={nome3:.2f} d={nome4:.3f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c, nome4=d
    ) 

print(formato)



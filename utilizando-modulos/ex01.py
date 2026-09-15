# Quebrando um número

from math import trunc
num = float(input('Digite um numero: '))
pt = trunc (num)
print('O numero {} tem a parte inteira {}'.format(num, pt))
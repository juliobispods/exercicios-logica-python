# Catetos e Hipotenusa

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot (co,ca)
# (co ** 2 + ca ** 2) ** (1/2) - formula matemática
print ('A hipotenusa vai medir {:.2f}'.format(hi))
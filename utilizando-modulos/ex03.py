# Seno, Cosseno e Tangente

from math import cos,sin, tan, radians
angulo = float(input('Digite um angulo: '))
seno = sin(radians (angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O valor de seno é {:.2f}, o de consseno é {:.2f} e o da tangente é {:.2f}'.format (seno, cosseno, tangente))
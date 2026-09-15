# Jogo de adivinhação

import random
n1 = int(input('Escolha um numero de 0 a 5: '))
num = random.randint(0,5)
if n1 == 'num':
    print('Você venceu!')
else:
    print('Você perdeu!')
# Sorteando uma ordem da lista

import random
a1 = str(input('Digite o nome do grupo 1: '))
a2 = str(input('Digite o nome do grupo 2: '))
a3 = str(input('Digite o nome do grupo 3: '))
a4 = str(input('Digite o nome do grupo 4: '))
lista = [a1, a2, a3, a4]
random.shuffle (lista)
print('A ordem das apresentações será: {} '.format(lista))
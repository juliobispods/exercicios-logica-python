# Ano Bissexto

import calendar
ano = int(input('Informe um ano: '))
if calendar.isleap(ano):
    print (f'O ano {ano} é bissexto')
else: 
    print (f'{ano} Não é bissexto')

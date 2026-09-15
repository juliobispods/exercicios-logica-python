# Aluguel de Carros

d = int(input('Informe a quantidade de dias alugados: '))
km = float(input('Informe a quantidade de Km percorrido: '))
diaria = (d * 60) + (km * 0.15)
print('O valor total a pagar é de R${:.2f} '.format(diaria))
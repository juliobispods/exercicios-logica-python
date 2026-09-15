# Custo da Viagem

n1 = float(input('Informe a distância da sua viagem em km:'))
if n1 <= 200:
    ps1 = n1 * 0.50
    print(f'O valor da sua passagem é de R$ {ps1:7.2f}')
else:
    n1 >= 200 
    ps2 = n1 * 0.45
    print(f'O valor da sua passagem é de R$ {ps2:7.2f}')
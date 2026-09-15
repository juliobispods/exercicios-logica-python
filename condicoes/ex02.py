# Radar eletronico

km = int(input('Digite a velocidade do carro: '))
if km >= 80:
    multa = (km - 80) * 7
    print(f'Voce foi multado em R$ {multa:7.2f}!')
else:
    print('Você esta dentro do limite de velocidade, boa viagem!')
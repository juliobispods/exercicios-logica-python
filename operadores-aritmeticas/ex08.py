# Calculando Descontos

p = float(input('Digite o preço do produto?:R$'))
d = p / 100
dr = d * 5
df = p - dr
# calculo certo = p - (p * 5 / 100)
print(f'Valor com desconto é {df:.2f}')
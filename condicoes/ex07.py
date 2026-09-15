# Aumentos múltiplos

sl = float(input('Informe o seu salário R$: '))
if sl > 1250.00:
    au = sl + (sl * 10 / 100)
else:
    sl <= 1250.00
    au = sl + (sl * 15 / 100)
print(f'Seu novo salário será de R$ {au:7.2f}')
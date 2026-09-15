# Analisando Triângulo

n1 = float(input('Informe o comprimento da reta 1: '))
n2 = float(input('Informe o comprimento da reta 2: '))
n3 = float(input('Informe o comprimento da reta 3: '))
if (n1 + n2 > n3) and (n1 + n2 > n3) and (n2 + n3 > n1):
    print('Sim! É possivel formar um triangulo')
else:
    print('Não! Não é possível formar um triângulo')
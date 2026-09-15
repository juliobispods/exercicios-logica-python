# Analisador de texto

nome = str(input('Digite seu nome completo: ')).strip()
print ('O seu nome maiusco é {}'.format(nome.upper()))
print ('O seu nome minusculo é {}'.format(nome.lower()))
print ('O seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print ('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print ('Seu primeiro nome é {} e ele tem {} letras'.format(separa [0], len(separa[0])))
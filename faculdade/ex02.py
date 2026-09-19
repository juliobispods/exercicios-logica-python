# Crie um algorito que leia uma lista de numero 
# inteiros e, caso haja numeros duplicados, considere
# apenas o primeiro deles, exemplo:
# Entrada: [7,8,4,7,4,3]
# Saída: [7,8,4,3]. Dica: use append() ou pop()

def removeDuplicados(lista):
    nova_lista = []
    for numero in lista:
        if numero not in nova_lista:
            nova_lista.append(numero)
    return nova_lista

entrada = [7, 8, 4, 7, 4, 3]
saida = removeDuplicados(entrada)
print(saida)


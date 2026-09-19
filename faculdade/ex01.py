# Desenvolva uma função que leia uma lista de número
# e um número alvo (target), retorne os 2 números de somados
# resultam no target

def twoSum(numbers, target):
    for i in range(len(numbers)):
        for j in range (i + 1, len(numbers)):
            if (numbers[i] + numbers[j] == target):
                return [numbers[i], numbers[j]]

listNumbers = [5, 4, 3, 5, 9,10]
targetNumber = 14
print (twoSum(listNumbers, targetNumber))
"""exercício 14"""

paes = int(input('Quantidade de pães vendidos: '))
bolos = int(input('Quantidade de bolos vendidos: '))

total = round((paes * 0.12) + (bolos * 1.5))

print (f'O valor a ser guardado na poupança é de R${total / 10}')
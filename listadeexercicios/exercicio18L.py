"""exercício 18"""

inicial = float(input('Salário do funcionário: R$'))

aumento = inicial + ((inicial / 100) * 15)

final = aumento - ((aumento / 100) * 8)

print (f'O salário inicial era R${inicial}, o salário depois do aumento é de R${aumento}, e depois do desconto dos impostos o salário final é de R${final}')
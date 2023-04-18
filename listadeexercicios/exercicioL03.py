"""Exercício 03"""

custofabrica = float(input('Digite o valor do custo de fábrica do carro: '))

distribuidor = (custofabrica / 100) * 28
imposto = (custofabrica / 100) * 45

final = custofabrica + distribuidor + imposto

print (f'A porcentagem do distribuidor é de R$: {distribuidor}.')
print (f'a porcentagem dos impostos é de R$: {imposto}.')
print (f'O valor do veículo para o consumidor vai ser de R${final}')
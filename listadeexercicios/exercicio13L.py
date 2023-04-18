"""exercício 13"""

custo = float(input('Preço de custo do produto: R$'))
percentual = float(input('Percentual de acréscimo: '))
venda = custo + ((custo / 100) * percentual)

print (f'O valor de venda do produto será de R${round(venda)}')
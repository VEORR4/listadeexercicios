"""exercício 21"""

valor = float(input('Valor da peça ou das peças compradas: R$'))
desconto = (valor / 100) * 30
final = valor - desconto

print (f'O valor a ser pago será R${final}.')
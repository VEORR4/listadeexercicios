"""exercício 11"""

valor = float(input('Valor depositado: '))
valorf = ((valor / 100) * 0.70) + valor

print (f'O valor total após 1 mês de rendimento é R${round(valorf)}')

valor = float(input('Valor depositado: '))
meses = int(input('Meses aplicado: '))
taxa = 0.007

montante = valor * ((1 + taxa) ** meses)

print (f'O montante ao final dos {meses} meses será R${round(montante)}. ')
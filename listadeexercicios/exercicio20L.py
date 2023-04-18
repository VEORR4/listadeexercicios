"""exercício 20"""

m1r = int(input('Quantidade de moedas de 1 real: '))
m50 = int(input('Quantidade de moedas de 50 centavos: ')) * 50
m25 = int(input('Quantidade de moedas de 25 centavos: ')) * 25
m10 = int(input('Quantidade de moedas de 10 centavos: ')) * 10
m5 = int(input('Quantidade de moedas de 5 centavos: ')) * 5
m1 = int(input('Quantidade de moedas de 1 centavo: ')) * 1

total = ((m50 + m25 + m10 + m5 + m1) / 100) + m1r

print (f'A quantidade total economizada foi de R${round(total)}.')
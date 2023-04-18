"""exercício 06"""

nome = input ('Digite o nome do aluno: ')
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Valor da segunda nota: '))
nota3 = float(input('Valor da terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print (f'A média das notas do aluno {nome} foi de : {media}')
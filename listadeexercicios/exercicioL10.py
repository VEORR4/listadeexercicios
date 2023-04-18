"""exercício 10"""


nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas do vendedor: "))

comissao = total_vendas * 0.15
salario_final = salario_fixo + comissao


print("Nome do vendedor: ", nome)
print("Salário fixo: R$", salario_fixo)
print("Salário final: R$", salario_final)
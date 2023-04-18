"""Exercício 1"""


dS = float(input('Variação de espaço (ponto de chegada - ponto de partida) em km:  '))
dt = float(input('Variação de tempo (tempo inicial - tempo final) em horas: '))
vm = dS / dt
print (f'A velocidade média do veículo é de {vm:.2f} km/h')
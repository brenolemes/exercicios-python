'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter
jogadas = {}
ranking = []
for c in range(1, 5):
    jogadas[f'jogador{c}'] = randint(1, 6)
print(jogadas)
print(f'Valores sorteados:')
for k, v in jogadas.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('-=' * 30)
print('Ranking dos jogadores:')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)  # Colocando em ordem decrescente as jogadas (número do dado - key=itemgetter(1)-+)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')



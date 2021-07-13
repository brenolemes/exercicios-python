'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print(f'{"JOGO DA MEGA CENA":^30}')
print('-' * 30)
n = int(str(input('Quantos jogos vecê quer que eu sorteie? ')))
print('-' * 7, f'SORTEANDO {n} JOGOS', '-' * 6)
for c in range(0, n):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.append(jogos[:])
    jogos.sort()
    jogos.clear()
    print(f'Jogo {c + 1}: {lista[c]}')
    sleep(1)
print('-' * 10, 'BOA SORTE!', '-' * 10)


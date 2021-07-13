'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla.
'''

from random import randint

aleatorio = (randint(0, 10), randint(0, 10), randint(0, 10),
             randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in aleatorio:
    print(n, end=' ')
print(f'\nO MENOR valor sorteado foi {min(aleatorio)}')     # min mostra qual é o menor número dentro de uma tupla
print(f'O MAIOR valor sorteado foi {max(aleatorio)}')   # # max mostra qual é o maior número dentro de uma tupla


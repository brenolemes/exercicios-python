# Escreva um programa que faça o computador "pensar" em um número inteiro...
# ...entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
oculto = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5')
print('-=-' * 20)
numero = int(input('Que número eu pensei: '))

print('PROCESSANDO')
sleep(3) # Vai demorar 3 segundos para que o programa continue

if numero == oculto:
    print('Parabens!! Você venceu!!')
else:
    print(f'Perdeu!! Eu Pensei no número {oculto} e não no número {numero}!!')


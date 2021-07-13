# Crie um programa que faça o computador jogar jokenpô com você

'''from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')




jogador = int(input('Qual é sua jogada? '))
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('=-=' * 15)
print(f'O computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('=-=' * 15)

if jogador == 0 and computador == 1:
    print(f'Você perdeu!!')
elif jogador == 1 and computador == 0:
    print('Você ganhou!!')
elif jogador == 0 and computador == 2:
    print('Você ganhou!!')
elif jogador == 2 and computador == 1:
    print('Vecê ganhou!!')
elif jogador == 1 and computador == 2:
    print('Você ganhou!!')
elif jogador == 2 and computador == 0:
    print('Você perdeu!!')
else:
    print('Deu empate!!')'''

from random import randint
from time import sleep

print('''Opções de jogadas:
[0] Pedra
[1] papel
[2] Tesoura''')

itens = ('Pedra', 'Papel', 'Tesoura')

jogador = int(input('Quais das opções você escolhe? '))
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('\033[1;30;43m=-=\033[m' * 11)
print(f'Você jogou \033[1;32m{itens[jogador]}\033[m')
print(f'O computador jogou \033[1;31m{itens[computador]}\033[m')
print('\033[1;30;43m=-=\033[m' * 11)

if computador == 0:
    if jogador == 0:
        print('\033[1;34mEMPATOU\033[m')
    elif jogador == 1:
        print('\033[1;32mVOCÊ VENCEU\033[m')
    elif jogador == 2:
        print('\033[1;31mVOCÊ PERDEU\033[m')

elif computador == 1:
    if jogador == 0:
        print('\033[1;31mVOCÊ PERDEU\033[m')
    elif jogador == 1:
        print('\033[1;34mEMPATOU\033[m')
    elif jogador == 2:
        print('\033[1;32VOCÊ GANHOU\033[m')

elif computador == 2:
    if jogador == 0:
        print('\033[1;32mVOCÊ GANHOU\033[m')
    elif jogador == 1:
        print('\033[1;31mVOCÊ PERDEU\033[m')
    elif jogador == 2:
        print('\033[1;34mEMPATOU\033[m')





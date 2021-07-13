'''
Molhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer
'''

'''
from random import randint
from time import sleep
computador = randint(1, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 1 a 10.')
print('Será que você consegue adivinhar qual foi? ')
jogador = int(input('Qual é seu palpite: '))
print('ANALISANDO...')
sleep(1)
palpites = 1
while jogador != computador:
    if jogador > computador:
        jogador = int(input('O número que pensei não foi MENOR. Tente novamente: '))
    elif jogador < computador:
        jogador = int(input('O número que pensei não foi MAIOR. Tente novamente: '))
    palpites += 1
    print('ANALISANDO...')
    sleep(2)
print(f'Acertou!! O número que eu escolhei foi {computador}.')
print(f'Foram necessários {palpites} palpites para você acertar.')
'''


# Outra forma de fazer (forma do Guanabara)
from random import randint
from time import sleep

computador = randint(1, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 1 e 10.
Será que você consegue adivinhar qual é? ''')
acertou = False # ou outra atruibuição qualquer
palpites = 0
while not acertou: # Leia como enquanto False, repita (while not x: == while False) e (while x: == while True)
    jogador = int(input('Digite um número: '))
    palpites += 1
    if jogador == computador:
        acertou = True # Quando virá verdeiro, é encerrada a repetição
    elif jogador > computador:
        print('O número que eu pensei foi MENOR.')
    elif jogador < computador:
        print('O número que eu pensei foi MAIOR.')
print(f'Parabéns!! Você acertou!!! Eu pensei no número {computador}')
print(f'Foram necessários {palpites} tentativas para você acertar.')


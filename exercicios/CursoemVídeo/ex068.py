'''
Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
'''

from random import randint
from time import sleep
'''
soma = 0
vitorias = 0
while True:
    jogador = str(input('Par ou Impar [p/i]? ')).strip().upper()[0]
    computador = randint(0, 10)
    n = int(input('Digite um número: '))
    print('-=-' * 20)
    print('PAR')
    sleep(1)
    print('OU')
    sleep(1)
    print('IMPAR')
    print('-=-' * 20)
    soma = n + computador
    if jogador == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador jogou {computador}. Total de {soma}, deu par')
            print('-=-' * 20)
            print(f'VOCÊ GANHOU!!')
            print('Vamos jogar novamente...')
            print('-=-' * 20)
            vitorias += 1
        else:
            print(f'Você jogou {n} e o computador jogou {computador}. Total de {soma}, deu impar')
            print('-=-' * 20)
            print('VOCÊ PERDEU!!')
            break
    elif jogador == 'I':
        if soma % 2 != 0:
            print(f'Você jogou {n} e o computador jogou {computador}. Total de {soma}, deu impar')
            print('-=-' * 20)
            print(f'VOCÊ GANHOU!!')
            print('Vamos jogar novamente...')
            print('-=-' * 20)
            vitorias += 1
        else:
            print(f'Você jogou {n} e o computador jogou {computador}. Total de {soma}, deu par')
            print('-=-' * 20)
            print('VOCÊ PERDEU!!')
            break
print(f'Você ganhou {vitorias} vez(es) consecutiva(s)!!')'''


# Forma do guanabara (forma com menos linhas)
v = 0
while True:
    jogador = int(input('Diga um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar: [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ GANHOU')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ GANHOU')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você venceu {v} vezes.')

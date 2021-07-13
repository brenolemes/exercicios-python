'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em
uma lista composta. No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
from time import sleep
alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])    # Dessa forma é mais facil pra adicionar porque já vai com tudo (nome, notas e a media)
    r = ' '
    while r not in 'NS':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break

print(f'{"BOLETIM DA TURMA":^30}')
print('=-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' * 30)
while True:
    opc = int(input(f'Mostrar notas de qual aluno (999 para parar): '))
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
    if opc == 999:
        print('FINALIZANDO...')
        sleep(2)
        break

print(f'<<<<<< VOLTE SEMPRE >>>>>>')
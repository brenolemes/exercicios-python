''' Faça um programa que tenha uma função chamada ficha(), que
receba dois parâmetros opcionais: o nome de um jogador e quantos gols
ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
que algum dado não tenha sido informado corretamente.'''


def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input(f'Nome do jogador: '))
gols = str(input(f'Número de gols: '))
if gols.isnumeric():    # verificando se a variável 'gols' é númerica, passar de str pra int
    gols = int(gols)
else:   # Se ela estiver vazia ou for uma string, transformar em valor int 0
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)

# REVISAR
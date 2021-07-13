'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for p in range(0, jogos):
        partidas.append(int(input(f'Quantos gols na partida {p}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    r = ' '
    while r not in 'NS':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('=-' * 30)
print(time)
print('-' * 45)
print('Cod. ', end='')
for v in jogador.keys():
    print(f'{v:<15} ', end='')
print()
print('-' * 45)
for k, v in enumerate(time):
    print(f'{k:<4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 45)

while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar)? '))
    if busca == 999:
        break
    if busca > len(time) - 1:
        print(f'ERRO! Não existe jogador com o codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADO {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i + 1} fez {g} gols. ')
    print('-' * 45)
print(f'<< VOLTE SEMPRE >>')

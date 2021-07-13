brasileirao11 = ('Corinthians', 'Vasco da gama', 'Fluminense', 'Flamengo', 'Internacional',
               'São Paulo', 'Figueirense', 'Coritiba', 'Botafogo', 'Santos', 'Palmeiras',
               'Grêmio', 'Atlético-GO', 'Bahia', 'Atlético-MG', 'Cruzeiro', 'Athletico-PR',
               'Ceará SC', 'América-MG', 'Avaí')
print('=' * 30)
for t in brasileirao11:
    print(t)
# print(f'Lista de times no brasileirão 2011 serie A')
print('=' * 30)
print(f'Os primeiros 5 primeiros colocados são {brasileirao11[:5]}')
print('=' * 30)
print(f'Os ultímos 4 colocados são {brasileirao11[-4:]}')
print('=' * 30)
print(f'Os times em ordem alfabética são {sorted(brasileirao11)}')
print('=' * 30)
print(f"O Flamengo está na {brasileirao11.index('Flamengo') + 1}ª posição")
print('=' * 30)


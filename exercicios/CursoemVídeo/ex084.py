'''
Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

'''
pessoas = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? ')).strip().upper()[0]
    if r in 'N':
        break
if len(pessoas) > 1:
    print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
else:
    print(f'Ao todo, foi cadastrada {len(pessoas)} pessoa.')
print(f'O maior peso foi de {maior}kg peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}kg peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')




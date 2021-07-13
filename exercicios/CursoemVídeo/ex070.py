'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
'''

gasto = 0
maior_mil = 0
menor = 0
cont = 0
mais_barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    gasto += preco
    if preco > 1000:
        maior_mil += 1
    if cont == 0 or preco < menor:  # forma com menos linhas
        menor = preco
        mais_barato = nome
    cont += 1
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja continuar comprando? [S/N] ')).strip().upper()[0]
    if mais in 'N':
        break
print('___' * 15)
print('FINAL DA COMPRA')
print('___' * 15)
print(f'O total gasto foi de R${gasto:.2f}')
print(f'{maior_mil} produto(s) custa(m) mais de mil reais')
print(f'O produto mais barato foi o(a) {mais_barato} que custa {menor:.2f}')

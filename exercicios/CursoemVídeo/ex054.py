'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date

maioridade = 0
menoridade = 0

for c in range(1, 8):
    ano = int(input('Qual ano você nasceu? '))
    idade = date.today().year - ano
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print(f'{maioridade} das 7 pessoas já atingiram a maioridade')
print(f'{menoridade} das 7 não atingiram a menoridade')




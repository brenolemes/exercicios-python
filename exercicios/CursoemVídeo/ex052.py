'''Faça um programa que leia um númeor inteiro e diga se ele é
ou não é primo.'''

tot = 0

num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[34m{c}\033[m', end=' ')
        tot += 1
    else:
        print(f'\033[32m{c}\033[m', end=' ')
if tot > 2:
    print(f'\nO número {num} foi divísivel {tot} vezes, portanto o número não é primo')
else:
    print(f'\nO número {num} é primo')

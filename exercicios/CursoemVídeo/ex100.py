'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função
anterior.
'''


from random import randint
numeros = list()


def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(1, 6):
        numeros.append(randint(1, 10))
    for v in numeros:
        print(f'{v}', end=' ')
    print(f'PRONTO!')


def somaPar(lst):
    soma = 0
    for c, v in enumerate(lst):
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lst}, temos {soma}')


sorteia()
somaPar(numeros)

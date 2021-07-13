'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da
função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep


'''def contador(inicio, fim, passo):
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim and passo < 0:
        if passo == 0:
            passo = 1
        for c in range(inicio, fim - 1, - (- passo)):
            print(f'{c}', end=' ')
            sleep(0.5)
        print('FIM')
    if inicio > fim:
        if passo == 0:
            passo = 1
        for c in range(inicio, fim - 1, - passo):
            print(f'{c}', end=' ')
            sleep(0.5)
        print('FIM')
    if inicio < fim:
        if passo == 0:
            passo = 1
        for c in range(inicio, fim + 1, passo):
            print(f'{c}', end=' ')
            sleep(0.5)
        print('FIM')


print('-=' * 30)
print(f'Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11, 1):
    print(f'{c}', end=' ')
print(f'FIM!')
print(f'{"-=" * 30}')
print(f'Contagem de 10 até 0 de 2 em 2')


for c in range(10, -1, -2):
    print(f'{c}', end=' ')
print(f'FIM!')
print('-=' * 30)
print(f'Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))'''


# Melhor forma (forma do guanabara)

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'=-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print(f'FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print(f'FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print(f'Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)

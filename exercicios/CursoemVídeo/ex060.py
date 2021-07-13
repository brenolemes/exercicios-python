'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
'''

'''n = int(input('Digite um número: '))
fat = 1
while n != 0:
    print(f'{n}', end=' ')
    fat *= n
    n -= 1
print(f'\nO fatorial é {fat}')'''

# formas do Guanabara (sem for e sem while)

'''from math import factorial
n = int(input('digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''

# formas do guanabara (com while)

'''n = int(input('Digite um número para calcular seu fatorial: '))
c = n
fat = 1
print(f'Calculando o fatorial de {n}! = ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(f'x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print(f'{fat}')'''

# formas do guanabara (com for)

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
fat = 1
print(f'Calculando o fatorial de {n}! = ', end='')
for c in range(c, 0, -1,):
    print(f'{c} ', end='')
    print(f'x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print(f'{fat}')

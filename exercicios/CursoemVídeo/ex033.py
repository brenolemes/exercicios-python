# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

menor = n1 # considerando que n1 é o menor número
if n2 < n1 and n2 < n3: # se o n2 for menor que o n1 e o n2
    menor = n2 # ele passa a ser o menor
if n3 < n1 and n3 < n2: # se o n3 for menor que n1 e o n2
    menor = n3 # ele passa a ser o menor
print(f'O MENOR valor digitado é o {menor}')
maior = n1 # Considerando n1 o maior valor
if n2 > n1 and n2 > n3: # se o n2 for maior que o n1 e o n3
    maior = n2 # ele passa a ser o maior
if n3 > n2 and n3> n1: # se o n3 for maior que o n1 e o n2
    maior = n3 # ele passa a ser o maior
print(f'O MAIOR valor digitado é o {maior}')

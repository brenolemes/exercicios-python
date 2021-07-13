'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

valores = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if mais == 'N':
        break
print(f'Você digitou {len(valores)} elemento(s)')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não foi encontrado na lista!')

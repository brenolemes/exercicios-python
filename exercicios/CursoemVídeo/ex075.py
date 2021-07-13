'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

num = (int(input('Digite número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não aparece em nenhuma posição')

print(f'Os valores pares digitados foram', end=' ')
for c in range(0, len(num)):
    if num[c] % 2 == 0:
            print(f'{num[c]}', end=' ')


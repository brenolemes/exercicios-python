'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''
num = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].insert(0, valor)     # Poderia dar um append
    elif valor % 2 != 0:
        num[1].insert(0, valor)     # Poderia dar um append
num[0].sort()   # Ordem crescente
num[1].sort()   # Ordem crescente
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')

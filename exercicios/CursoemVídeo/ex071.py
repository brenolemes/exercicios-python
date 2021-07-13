'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e de R$1.
'''
'''soma = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
valor = int(input('Qual valor deseja sacar? '))
while True:
    if valor >= 50:
        valor = valor - 50
        cont50 += 1
    elif valor >= 20:
        valor = valor - 20
        cont20 += 1
    elif valor >= 10:
        valor = valor - 10
        cont10 += 1
    elif valor >= 1:
        valor = valor - 1
        cont1 += 1
    if valor == 0:
        break
print('-=-' * 15)
if cont50 > 0:
    print(f'O total de notas de R$50 impressas foi de {cont50}')
if cont20 > 0:
    print(f'O total de notas de R$20 impressas foi de {cont20}')
if cont10 > 0:
    print(f'O total de notas de R$10 impressas foi de {cont10}')
if cont1 > 0:
    print(f'O total de notas de R$1 impressas foi de {cont1}')
print('-=-' * 15)'''


# Forma do guanabara (melhor forma)

valor = int(input('Qual valor deseja sacar? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

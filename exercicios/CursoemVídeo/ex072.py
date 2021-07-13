'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso
'''

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
       'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
       'dezesseis', 'dezesete', 'dezoito', 'dozenove', 'vinte')

while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {num[n]}')
    mais = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if mais in 'N':
        break
print('Programa ecerrado. Volte sempre!!!')

# Forma do guanabara


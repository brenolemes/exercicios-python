''' Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- P primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais '''

from datetime import date
print('\033[1;33m--=--\033[m' * 20)
print('\033[1;30mANALISANDO QUAL É U NÚMERO MAIOR\033[m')
print('\033[1;33m--=--\033[m' * 20)

from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print(f'Primeiro número {n1}')
print(f'Segundo número {n2}')
if n1 > n2:
    print('\033[1;32mANALISANDO...\033[m')
    sleep(2)
    print('O primeiro valor é maior!!')
elif n2 > n1:
    print('\033[1;32mANALISANDO...\033[m')
    sleep(2)
    print('O segundo número é maior!!')
else:
    print('\033[1;32mANALISANDO...\033[m')
    sleep(2)
    print('Os dois números são iguais!!')

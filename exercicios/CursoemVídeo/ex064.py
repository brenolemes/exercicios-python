'''
Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''

'''n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
        cont += 1
print(f'A soma dos {cont} números digitados é {soma}')'''


# Formas do guanabara

soma = cont = 0
n = int(input('Digite um número inteiro (999 para parar): '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro (999 para parar): '))
print(f'A soma dos {cont} números digitados é {soma}')

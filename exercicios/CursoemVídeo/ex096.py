'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def area(l, c):
    area = c * l
    print(f'A área de um terreno {a}x{l} é de {area}m².')


titulo(' Controle de Terreno')
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))  #Poderia ter feito variáveis com inputs e passadas como parametros





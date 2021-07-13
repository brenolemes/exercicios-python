'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

from datetime import datetime


def voto(nasc):
    idade = datetime.now().year - nasc
    if idade >= 18 and idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade >= 16 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO NEGADO.'


ano = int(input('Em que ano você nasceu? '))
resp = voto(ano)
print(f'{voto(ano)}')

print(' '.join(map(str, resp)))


'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime
pessoas = {}
pessoas['nome'] = str(input('Nome: ')).strip()
ano = int(input('Ano de nascimento: '))
pessoas['idade'] = datetime.now().year - ano    # (Outra forma de fazer)
pessoas['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoas['ctps'] != 0:
    pessoas['contratação'] = int(input('Ano de contratação: '))
    pessoas['salário'] = float(input('Salário: R$'))
    pessoas['aposentadoria'] = pessoas['idade'] + ((pessoas['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
print(pessoas)
for k, v in pessoas.items():
    print(f'- {k} tem o valor {v}')


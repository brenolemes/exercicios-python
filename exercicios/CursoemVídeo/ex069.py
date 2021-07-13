'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados
c Quantas mulheres tem menos de 20 anos.
'''

soma_idade = 0
soma_homens = 0
idade_mulheres = 0
cont = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'M':
            soma_homens += 1
    else:
        if idade < 20:
            idade_mulheres += 1
    if idade >= 18:
        soma_idade += 1
    cont += 1
    print('-=-' * 20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar cadastrando? ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 20)
print(f'No total foram cadastradas {cont} pessoas')
print(f'{soma_idade} pessoa(s) são maior(es) de idade')
print(f'{soma_homens} homem(s) foram cadastrados')
print(f'{idade_mulheres} mulhere(s) tem menos de 20 anos')

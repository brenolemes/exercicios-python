'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

dados = {}
lista = []
lista_mulheres = []
lista_acima_media = []
soma = media = 0
while True:
    dados.clear()   # Não é obrigatório limpar o dicionário, poís ele faz trocas a cada iteração, não da append.
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    if dados['sexo'] in "F":
        lista_mulheres.append(dados['nome'])
    r = ' '
    while r not in "NS":
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r in "N":
        break
print(lista)
print(f'- O grupo tem {len(lista)} pessoas.')
media = soma / len(lista)
print(f'- A média de idade é de {media:.2f} anos')
print(f'- As mulheres cadastradas foram: ', end='')
for v in lista_mulheres:
    print(v, end=' ')
for c, v in enumerate(lista):
    if lista[c]['idade'] > media:
        lista_acima_media.append(lista[c])
print(f'\n- Lista das pessoas com idade acima da média:')
print()
for c, v in enumerate(lista_acima_media):
    print(f'Nome = {lista_acima_media[c]["nome"]}; sexo = {lista_acima_media[c]["sexo"]}; idade = {lista_acima_media[c]["idade"]};')
    print()
print('<< ENCERRADO >>')


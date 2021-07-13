'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'-------- {c}ª Pessoa --------')
    nome = str(input('Qual é o seu nome? ')).strip()
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Qual é o seu sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in'mM':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Neste grupo temos {totmulher20} mulher(s) com menos de 20 anos')

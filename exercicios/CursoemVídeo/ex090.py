'''
Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

matematica = {}
matematica['Nome'] = str(input("Nome: "))
matematica['Média'] = float(input(f'Média de {matematica["Nome"]}: '))
if matematica['Média'] >= 7.0:
    matematica['situação'] = 'Aprovado'
elif matematica['Média'] <= 4:
    matematica['situação'] = 'Recuperação'
else:
    matematica['situação'] = 'Reprovado'
print('-=' * 30)
for n in matematica.items():
    print(f'{n[0]} é igual {n[1]}')

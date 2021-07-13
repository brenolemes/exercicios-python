''' Crie um programa que leia duas notas de um aluno e calcule sua média. Moatrando uma mensagem no final.
De acordo com a média atingida '''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f} a média é {media:.1f}')
if media < 5.0:
    print('REPROVADO!!')
elif media >= 5.0 and media < 7.0: # outra forma e mais legivel: 7 > media >= 5:
    print('RECUPERAÇÃO!!')
else:
    print('APROVADO!!')

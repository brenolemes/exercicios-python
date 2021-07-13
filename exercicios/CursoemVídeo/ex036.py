''' Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''

valor = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário? R$'))
anos = int(input('Em quantos anos vai pagar a casa? '))
prestacao = valor / (anos * 12)
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')

if prestacao <= salario * 0.30:
    print("Seu empréstimo foi aprovado com sucesso!!")
else:
    print('Seu empréstimo não foi aprovado!!')

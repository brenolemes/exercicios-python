# Faça um algorítmo que leia um salário de um funcíonario de mostre seu salário com 15% de aumento

nome = str(input('Qual é o seu nome? '))
salario = float(input('Qual é o seu salário? '))
aumento = salario * 0.15
salario_novo = salario + (salario * 15 / 100)
print('Parabéns, {}!!!! você teve um aumento de R${:.2f}. Agora seu salário é R${:.2f}'.format(nome, aumento, salario_novo))

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1250, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário? '))

if salario > 1250:
    salario2 = salario + (salario * 0.10)
    aumento = salario2 - salario
else:
    salario2 = salario + (salario * 0.15)
    aumento = salario2 - salario
print(f'Você teve um aumeto de {aumento:.2f} e seu salario agora é de R${salario2:.2f}')

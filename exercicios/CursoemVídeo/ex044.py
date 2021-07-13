# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# á vista dinheiro/cheque: 10% de desconto
# á vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais mo cartão: 20% de juros

valor = float(input('Qual o valor do produto? '))

print('''Forma de pagamento:
[1] à vista dinheiro
[2] à vista cheque
[3] à vista no cartão
[4] 2x no cartão
[5] 3x ou mais''')
forma = input('Qual é a opção? ')
print(f'O valor do produto é R${valor:.2f}')


if forma == '1':
    dinheiro = valor - (valor * 0.10)
    print(f'A forma de pagamento vai ser em dinheiro. Você terá 10% de desconto, portanto pagará R${dinheiro:.2f}!')
elif forma == '2':
    cheque = valor - (valor * 0.10)
    print(f'A forma de pagamento vai ser em cheque. Você terá 10% de desconto, portanto pagará R${cheque:.2f}!')
elif forma == '3':
    cartao = valor - (valor * 0.05)
    print(f'A forma de pagamento vai ser no cartão à vista. Você terá desconto de 5%, portanto pagará R${cartao:.2f}')
elif forma == '4':
    cartao2 = valor
    print(f'A forma de pagamento vai ser no cartão em 2x. Você não terá desconto, portanto pagará R${cartao2:.2f}!')
elif forma == '5':
    cartao3 = valor + (valor * 0.20)
    print(f'A forma de pagamento vai ser no cartão em 3x ou mais. Você terá 20% de juros, portanto pagará R${cartao3:.2f}!')
else:
    print('Opção inválida. tente novamente.')

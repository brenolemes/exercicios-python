# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
# Valor_original - (valor_original * 5 / 100) == valor atual do produto menos 5% do valor atual do produto

valor_original = float(input('Qual o preço do produto? R$'))
valor_descontado = valor_original * 0.05
novo_valor = valor_original - (valor_original * 5 / 100)
print('O produto com valor de R${:.2f} na promoção, com 5% de desconto fica com o valor de R${:.2f}. Obtendo R${} de desconto'.format(valor_original, novo_valor, valor_descontado))


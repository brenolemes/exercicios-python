# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h. Mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite

velocidade = int(input('Qual é a velocidade do carro? '))
print(f'A velocidade foi de {velocidade}km/h')
if velocidade > 80:
    print('Você foi multado!!')
    print(f'A multa que você terá que pagar é de R${(velocidade - 80) * 7}')
    print('A multa custa R$7,00 por cada km acima do limite')
print('Tenha um bom dia, dirija com segurança!!!')

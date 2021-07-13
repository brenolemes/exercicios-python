# Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule se IMC e mostre
# Seu status, de acordo com a tavela abaixo:
# Abaixo de 18.5: abaixo do peos
# Entre 18.5 e 25: peso ideal
# 25 até 30: sobre peso
# 30 até 40: obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O imc dessa pessoa é de \033[1;34m{imc:.1f}\033[m')
if imc < 18.5:
    print('\033[1;33mAbaixo do peso!!\033[m')
elif imc <= 25:
    print('\033[1;32mPeso ideal!!')
elif imc <= 30:
    print('\033[1;34mSobrepeso!!\033[m')
elif imc <= 40:
    print('\033[1;31mObesidade!!\033[m')
else:
    print('\033[1;30mObesidade mórbida!!\033[m')

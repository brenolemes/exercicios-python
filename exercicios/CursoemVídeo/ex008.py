# Escreva um programa que leia um valor em métros e o exiba convertido em centímetros e milímitros

n1 = float(input('Dígite um valor em cm: '))
print('O valor {:.0f}m em centímetros é {}cm e em milímitros é {}mm'.format(n1, (n1 * 100), (n1 * 1000)))

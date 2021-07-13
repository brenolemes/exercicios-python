# Escreva um programa que copnverta uma temperatura em °C para °F
# Formula da conversão de °C para °F

c = float(input('Informe a temperatura: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))

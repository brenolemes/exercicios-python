# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
ca = float(input('valor do o cateto oposto: '))
co = float(input('Valor do cateto adjacente: '))
h = (co**2 + ca**2) ** (1/2)
h2 = hypot(co, ca)
print('A hipotenusa do triângulo com cateto adjacente de {:.2f} e cateto oposto de {:.2f} é {:.2f}'.format(ca, co, h))
print(f"Utilizando módulo: {h2:.2f}")

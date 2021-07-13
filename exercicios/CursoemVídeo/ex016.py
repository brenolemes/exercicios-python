# Crie um programa que leia um número Real qualquer e mostre na tela a sua porção inteira.

import math
num = float(input('Dígite um número: '))
print('A porção inteira do número {} é {}'.format(num, math.trunc(num)))


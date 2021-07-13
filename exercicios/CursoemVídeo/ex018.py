# Faça um programa que leia um algulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse triângulo

import math
x = float(input('Qual o algulo do triângulo? '))
seno = math.sin(math.radians(x))
cosseno = math.cos(math.radians(x))
tangente = math.tan(math.radians(x))

print(f'O seno, o cossseno e a tengênte em radianos do angulo de {x} é, respectivamente, {seno:.2f}, {cosseno:.2f} e {tangente:.2f}')


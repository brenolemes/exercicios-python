# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo serpa formado
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = float(input('Qual é o primeriro segmento? '))
r2 = float(input('Qual é o segundo segmento? '))
r3 = float(input('Qual é o terceiro segmento? '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos \033[1;32mPODEM\033[m formar um triângulo!!')
    if r2 == r1 == r3: # outra forma: r1 == r2 and r2 == r3
        print('Esse triângulo é \033[1;34mequilátero\033[m')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Esse triângulo é \033[1:34misósceles\033[m')
    elif r1 != r2 != r3 != r1: # outra forma: r1 != r2 and r2 != r3 and r3 != r1 ou usar o else
        print('Esse triângulo é \033[1;34mescaleno\033[m')
else:
    print('Os segmantos \033[1;31mNÃO\033[m podem formar um triângulo!!!')

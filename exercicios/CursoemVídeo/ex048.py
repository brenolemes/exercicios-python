'''Faça um programa que calcule a soma entre todos os números
 impares que são múltiplos de três e que se encontram no
 intervalo de 1 a 500'''

'''s = 0
cont = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
    cont += 1
        s += c
print(f'A soma dos números múltiplos de 3 no intevalor de 1 a 500 é de {s}!')'''

# outra forma de fazer
# forma com menos laços (melhor)

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} números solicitados é {soma}!!')

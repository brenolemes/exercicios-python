'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna3 = 0
maior = menor = 0
for l in range(3):
    matriz.append([])
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_coluna3 += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = menor = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]
                if matriz[l][c] < menor:
                    menor = matriz[l][c]
print('-=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}')
print(f'O maior valor da segunda linha é {maior}')
print(f'O menor valor da segunda linha é {menor}')

# Outra forma de achar a soma da terceira coluna
'''
for l in range(0, 3):
    soma_coluna3 += matriz[l][2]
'''

# Outra forma de achar o maior e o menor valor da segunda linda
'''
for c in range(0, 3):
    if c == 0:
        maior = menor = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
        if matriz[1][c] < menor:
            menor = matriz[1][c]
'''




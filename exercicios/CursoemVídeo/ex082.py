valores = []
valores_pares = []
valores_impares = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if mais == 'N':
        break
for c in range(0, len(valores)):
    if valores[c] % 2 == 0 and valores[c] != 0:
        valores_pares.append(valores[c])
    elif valores[c] % 2 != 0 and valores[c] != 0:
        valores_impares.append(valores[c])
print('-=' * 30)
print(f'A lista completa é: {valores}')
print(f'A lista de pares é: {valores_pares}')
print(f'A lista de impares é: {valores_impares}')

'''Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for impar, desconcidere-o'''

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você me informar {cont} números pares e soma dos valores pares é {soma}')

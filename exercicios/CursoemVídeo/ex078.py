'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foio maior e o menor valor digitado e as suas respectivas
posições na lista.
'''

valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-' * 40)
print(f'Você digitou os valores {valores}')
print(f'O MAIOR valor digitado foi {maior} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}... ', end='')
print(f'\nO MENOR valor digitado foi {menor} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}... ', end='')

'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o menor e o maior peso lidos'''

'''maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa? (kg)'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'A pessoa com mais peso tem {maior}kg e a pessoa com menos peso tem {menor}kg')'''

# outra forma de fazer: usando os elif's e não as identações
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa? (kg)'))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
            maior = peso
    elif peso < menor:
            menor = peso
print(f'A pessoa com mais peso tem {maior}kg e a pessoa com menos peso tem {menor}kg')



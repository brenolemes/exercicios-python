'''Faça um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão'''

'''termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão dessa PA: '))

print(termo)
for c in range(1, 10):
    termo += razao
    print(termo)'''


primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end=' » ')
print('ACABOU!!')

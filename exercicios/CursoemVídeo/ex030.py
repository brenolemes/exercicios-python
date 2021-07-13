# Crie um programa que leia um numero inteiro e mostre na tela se le é par ou impar

n = int(input('Digite um numero inteiro: '))
print(f'O numero digitado foi {n}')
if n % 2 == 0:
    print('Este número é par!')
else:
    print('Esse número é ímpar!!')

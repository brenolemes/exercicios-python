'''
Crie um programa que leia varios números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores lidos.
O programa deve perguntar au usuário se ele quer ou não continuar a digitar valores.
'''

'''soma = 0
maior = 0
menor = 0
cont = 0

while True:
    n = int(input('Digite um número inteiro: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    novo = str(input('Deseja continuar a digitar [S/N]: ')).strip().upper()
    if novo in 'N':
        break
    else:
        continue
media = soma/cont
print(f'A média do(s) {cont} número(s) digitados é {media:.2f}')
print(f'O menor valor digitado foi {menor} e o maior foi {maior}')'''


# Outra forma de fazer (forma do guanabara)

res = 'sS'
soma = quant = maior = menor = 0
while res in 'sS':
    n = int(input('Digite um número inteiro: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'A média dos {quant} números digitados é de {media}')
print(f'O menor valor digitado foi {menor} e o maior foi {maior}')

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

# Forma srt de fazer

n = (input('Dígite um número de 0 a 9999: '))

if len(n) == 4:
    unidade = n[3]
    dezena = n[2]
    centena = n[1]
    milhar = n[0]
    print(unidade)
    print(dezena)
    print(centena)
    print(milhar)
if len(n) == 3:
    unidade = n[2]
    dezena = n[1]
    centena = n[0]
    print(unidade)
    print(dezena)
    print(centena)
if len(n) == 2:
    unidade = n[1]
    dezena = n[0]
    print(unidade)
    print(dezena)
if len(n) == 1:
    unidade = n[0]
    print(unidade)

    # forma numérica de fazer

''' n = int(input('Dígite um número de 1 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena:{c}')
print(f'milhar:{m}') '''

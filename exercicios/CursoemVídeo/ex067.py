'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O progrma será interrompido quando o número solicitado for negativo
'''

cont = 1
produto = 0
n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor (número negativo para parar): '))
    if n < 0:
        break
    while cont <= 10:
        produto = n * cont
        print(f'{n:2} x {cont:2} = {produto:2}')
        cont += 1
    cont = 0
print('Programa ecerrado. Volte sempre.')

# forma do guanabara e a melhor (usando for)
'''n = 0
while True:
    n = int(input('Quer saber a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n:2} x {c:2} = {n * c:2}')
print('Programa ecerrado. Volte sempre.')'''



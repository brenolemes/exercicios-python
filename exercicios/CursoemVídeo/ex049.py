'''Refaça o exercício 009, mostrando a tabuada de um número que o
usuário escolher, só que agora utilizando um laço for'''

n = int(input('Qual número quer saber a tabuada? '))
for c in range(1, 11):
    print(f'{n:2} x {c:2} = {n * c:2}')

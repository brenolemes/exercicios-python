# Um professor quer sortear um dos seus quatro alunos pra apagar o quadro. faça um programa que ajude ele lendo os nome deles e escrevendo o nome do escolhido

import random

nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo aluno: '))
nome3 = str(input('nome do terceiro aluno: '))
nome4 = str(input('Nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
print(f' A pessoa sortada foi o(a) {random.choice(lista)}!!!!')

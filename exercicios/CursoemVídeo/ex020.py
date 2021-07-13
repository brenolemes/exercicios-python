# O mesmo prfessor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

'''import random

nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo aluno: '))
nome3 = str(input('nome do terceiro aluno: '))
nome4 = str(input('Nome do quarto aluno: '))
lista_nome = [nome1, nome2, nome3, nome4]
random.shuffle(lista_nome)
print('A ordem de apresentação será: ')
print(lista_nome)'''

# Programa que sorteia um time pra cada jogador

from random import shuffle

nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo aluno: '))
nome3 = str(input('nome do terceiro aluno: '))
nome4 = str(input('Nome do quarto aluno: '))
lista_nome = [nome1, nome2, nome3, nome4]
shuffle(lista_nome)

t1 = str(input('Escollha um time: '))
t2 = str(input('Escolha outro time: '))
t3 = str(input('Escolha outro time: '))
t4 = str(input('Escolha outro time: '))
lista_time = [t1, t2, t3, t4]
shuffle(lista_time)
print('Os times selecionados pra cada um é: ')
print(lista_nome)
print(lista_time)



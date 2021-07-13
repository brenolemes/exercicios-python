# Crie um programa que leia o nome completo de uma pessoa e mostre seu primeiro nome e o ultimo

nome = str(input('Qual é o seu nome completo? ')).strip()
dividido = nome.split()
print(f'Primeiro: {dividido[0]}')
print(f'Último: {dividido[len(dividido) - 1]}') # Me mostra o ultimo da lista == dividido[len(dividido) - 1]


# Crie um progama que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maíusculas 1
# O nome com todas as letras minúsculas 1
# Quantas letras tem no total (desconciderando os espaços) 0
# Quantas letras tem o primeira nome 1

nome = str(input('Qual é o seu nome? ')).strip()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f"Seu nome tem {len(nome) - nome.count(' ')}")
nome_dividido = nome.split()
print(f'Seu primeiro nome é {nome_dividido[0]} e ele tem {len(nome_dividido[0])} letras')
# print(f"Seu primeiro tem {nome.find(' ')} letras")


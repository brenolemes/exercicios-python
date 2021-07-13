'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
Caso esteja errado, peça a digitação novamente até ter um valor correto
'''

# Validando dados
# Enquanto não digitar corretamente o que esta perguntando, ele repete a pergunta
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Sexo inválido. Por favor, digite seu sexo novamente: ')).strip().upper()[0]
print('Seu sexo foi registrado com secesso!!')

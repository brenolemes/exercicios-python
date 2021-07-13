''' Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal '''

n = int(input('Digite um número inteiro: '))
print('''escolha uma das bases para conversão:
[1] converter para BANÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{n} convertido para BINÁRIO é {bin(n)[2:]}') # Usando fatiamento para retirar os dois primeiros digitos ([2:])
elif opcao == 2:
    print(f'{n} convertido para OCTAL é {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para HEXADECIMAL é {hex(n)[2:]}')
else:
    print('Opção inválida, tente novamente.')

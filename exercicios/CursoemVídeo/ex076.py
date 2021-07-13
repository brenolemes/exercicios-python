'''
Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência. No final, mostre uma
listagem de preços, organizando os dados em forma tabular.
'''

'''listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 32)
print(f'LISTAGEM DE PREÇOS')
print('-' * 32)
print(f'{listagem[0]}....................R${listagem[1]:5.2f}
{listagem[2]}.................R${listagem[3]:5.2f}
{listagem[4]}..................R${listagem[5]:5.2f}
{listagem[6]}...................R${listagem[7]:5.2f}
{listagem[8]}.............R${listagem[9]:5.2f}
{listagem[10]}.................R${listagem[11]:5.2f}
{listagem[12]}..................R${listagem[13]:5.2f}
{listagem[14]}..................R${listagem[15]:5.2f}
{listagem[16]}....................R${listagem[17]:5.2f}')
print('-' * 32)'''

# Forma do gunabara COM UM COMPLEMENTO MEU (melhor forma)

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DA COMPRA":^40}')
print('-' * 40)
soma = 0
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end='')
    else:
        soma += listagem[c]
        print(f'R${listagem[c]:>7.2f}')
print('-' * 40)
print(f'{"Total":.<30}', end='')
print(f'R${soma:>7}')
print('-' * 40)

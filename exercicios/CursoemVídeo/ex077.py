'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
'''palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')'''


'''print(f'Na palavra APRENDER temos ', end='')
for c in range(0, len(palavras[0])):
    if palavras[0][c] in 'aeiou':
        print(palavras[0][c], end=' ')

print(f'\nNa palavra PROGRAMAR temos ', end='')
for c in range(0, len(palavras[1])):
    if palavras[1][c] in 'aeiou':
        print(palavras[1][c], end=' ')

print(f'\nNa palavra LINGUAGEM temos ', end='')
for c in range(0, len(palavras[2])):
    if palavras[2][c] in 'aeiou':
        print(palavras[2][c], end=' ')

print(f'\nNa palavra PYTHON temos ', end='')
for c in range(0, len(palavras[3])):
    if palavras[3][c] in 'aeiou':
        print(palavras[3][c], end=' ')

print(f'\nNa palavra CURSO temos ', end='')
for c in range(0, len(palavras[4])):
    if palavras[4][c] in 'aeiou':
        print(palavras[4][c], end=' ')

print(f'\nNa palavra GRATIS temos ', end='')
for c in range(0, len(palavras[5])):
    if palavras[5][c] in 'aeiou':
        print(palavras[5][c], end=' ')

print(f'\nNa palavra ESTUDAR temos ', end='')
for c in range(0, len(palavras[6])):
    if palavras[6][c] in 'aeiou':
        print(palavras[6][c], end=' ')

print(f'\nNa palavra PRATICAR temos ', end='')
for c in range(0, len(palavras[7])):
    if palavras[7][c] in 'aeiou':
        print(palavras[7][c], end=' ')

print(f'\nNa palavra TRABALHAR temos ', end='')
for c in range(0, len(palavras[8])):
    if palavras[8][c] in 'aeiou':
        print(palavras[8][c], end=' ')

print(f'\nNa palavra MERCADO temos ', end='')
for c in range(0, len(palavras[9])):
    if palavras[9][c] in 'aeiou':
        print(palavras[9][c], end=' ')

print(f'\nNa palavra PROGRAMADOR temos ', end='')
for c in range(0, len(palavras[10])):
    if palavras[10][c] in 'aeiou':
        print(palavras[10][c], end=' ')

print(f'\nNa palavra FUTURO temos ', end='')
for c in range(0, len(palavras[11])):
    if palavras[11][c] in 'aeiou':
        print(palavras[11][c], end=' ')'''

# Forma do guanabara (melhor forma)

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

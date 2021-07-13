expr = str(input('Digite a expressão: ')).strip()
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'Sua expressão está válida')
else:
    print(f'Sua expressão está errada')

# Forma que um seguidor do guanabara fez
'''lista = list(input('Digite a sua equação, meu caro ser humano! '))
c1 = 0
for c in lista:
    if c == '(':
        c1 += 1
    if c == ')':
        c1 -= 1
    if c1 < 0:
        break
if c1 != 0:
    print('A equação não está correta!')
if c1 == 0:
    print('A equação está correta!'''

'''O algoritmo faz com que pra cada parentese fechando (')') elimine um abrindo.
E se a pilha for igual a 0, significa que o número de parênteses abrindo ('(') é o mesmo dos parênteses fechado (')')
Assim, validando a expressão.
Caso contrario, ou seja, se a pilha for maior do que 0, significa que o número de parenteses fechando e o número de 
parenteses abrindo são diferentes.
'''

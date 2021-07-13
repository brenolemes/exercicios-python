'''
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
As tuplas são variáveis compostas e imutáveis que permitem armazenar
vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''

'''lanche = ('Hamburguer', 'Suco', 'pizza', 'pudim')

# Todos os tipos de for, utilizando as variáveis compostas (tuplas)
for comida in lanche:   # não é possível mostrar a posição
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):  # É possível mostrar a posição
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):   # É possível mostrar a posição
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!!!')

print(sorted(lanche))   # Mostra a tupla em ordem alfabética no formado de lista'''


'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a   # Junta as tuplas, tornando uma só com os elementos do A e do B
print(c)
print(c.count(4))   # Mostra quantos vezes aparece o elemento 4 na tupla C
print(c.index(5))   # Mostra em qual index esta o elemento 5 na tupla C
print(c.index(5, 1))    # Mostra em qual indice esta o elemento 5 considerando a partir do indice 1 (eliminando o indice 0 onde esta o primeiro 5)'''

# AS TUPLAS SÃO IMUTÁVEIS
'''A unica coisa que pode fazer é apagar a variável composta (tupla) por completa
pessoas = ('Gustavo', 39, 'M', 99.98)
del(pessoas)
print(pessoas)  # Vai me retornar um erro porque foi apagada a tupla por completo'''

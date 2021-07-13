'''
Nessa aula, vamos aprender o que são LISTAS e como utilizar
listas em Python. As listas são variáveis compostas que permitem
armazenar vários valores em uma mesma estrutura, acessíveis
por chaves individuais.
'''
'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()  # ordena na sequencia do menor para o maior ou de A a Z
num.sort(reverse=True)  # ordena na sequencia do maior para o menor ou de Z a A
num.insert(2, 2)    # adicionando o 0 no indice 2
num.pop(2)  # remove o número que esta no indice 2
num.remove(2)   # Remove o primeiro elemento 2 (Se tiver mais de um 2 e quiser eliminar eles, só usar laços)
print(f'Esse lista tem {len(num)} elementos.')  # Mostra quantos elementos tem dentro da lista
# Tentando remover um número que não esta na lista
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)'''

'''# Criando uma lista de outra forma
valores = []    # É possivel criar da seguinte forma >>> valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Cheguei ao final da lista.')'''

'''# Criando outra lista de outra forma
valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c in range(0, len(valores)):
    print(f'Na posição {c} encontrei o valor {valores[c]}!')
print(f'Cheguei ao final da lista.')'''

a = [2, 3, 4, 7]
b = a   # Fazendo uma ligação entre A e B (Caso queira alterar uma, vai alterar a outra junto)
b[2] = 8    # Troca o valor do A e do B no indice 2, por 8
b = a[:]    # Aqui não existe ligação, o B vira uma copia do A
b[2] = 8
print(f'Lista a: {a}')
print(f'Lista b: {b}')

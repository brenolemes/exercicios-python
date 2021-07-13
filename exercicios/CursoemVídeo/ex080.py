'''
Crie um programa onde o usuário possa digitar cinco valores
numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista
ordenada na tela.
'''

valores = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        valores.append(n)
        print(f'Adicionado ao final da lista')
    elif n > valores[-1]:
        valores.append(n)
        print(f'Adicionado ao final da lista')
    else:   # Se não é o primeiro número a ser digitado e não é maior que o ultimo número da lista
        pos = 0
        while pos < len(valores):   # while True também da certo (e talvez seria até melhor)
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')


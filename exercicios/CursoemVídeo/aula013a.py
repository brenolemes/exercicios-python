# Estrutura de repetição FOR

s = 0 # declarando que s é 0
for c in range(0, 4): # c é o contador e o (0, 4) exclui o ultimo número. Vai repetir 4 vezes
    n = int(input('Digite um número: ')) # Vai perguntar 4 vezes
    s += n # a cada repetição é acrescentado ao s o valor digitado
print(f'O somatório dos números foi {s}') # Vai acontecer uma vez porque está fora do laço FOR
print('FIM')

# teste:
for c in range(6, 0, -1): # for c in range(6, 0, -1) vai de 6 a 1 (Ao contrario)
    print(c)

for c in range(0, 6, 2): # for c in range (0, 4, 2) faz com que pule de 2 em 2
    print(c)

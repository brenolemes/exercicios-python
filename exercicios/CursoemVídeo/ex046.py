# Faça um programa que mostre na tela uma contagem regrassiva para o estouro de fogos
# de atifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Feliz ano novoooo!!!!')

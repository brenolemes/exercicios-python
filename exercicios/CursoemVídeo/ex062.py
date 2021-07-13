'''
Molhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

primeiro = int(input('Digite o primeiro termo: '))
termo = primeiro
razao = int(input('Digite a razão: '))
cont = 1
mais = 10 # recebe 10 porque na primeira iteração pede pra mostrar 10 termos
total = 0
while mais != 0:
    total += mais # o total vai recebendo a soma de mais a cada iteração
    while cont <= total: # na primeira iteração, o total vale 10
        print(f'{termo} ', end='')
        print(f'>> ' if cont < total else '', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print(total)














    # Utilizando o for após o if
'''for cont in range(cont, novos_termos + 10):
            print(f'{termo} ', end=' >> ')
            termo += razao
            cont += 1'''

'''if cont == 11:
            novos_termos = int(input('\nQuer que mostre mais quantos termos? '))
            while cont <= novos_termos + 10:
                print(f'{termo} ', end='')
                print(f'>> ' if cont < novos_termos + 10 else '', end='')
                termo += razao
                cont += 1'''


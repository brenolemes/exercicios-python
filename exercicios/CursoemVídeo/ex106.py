from time import sleep


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    titulo(f'Acessando o manual do comando \"{com}\"', 4)
    print(f'{c[6]}', end='')
    help(com)
    print(f'{c[0]}', end='')
    sleep(2)


# Programa principal
c = ('\033[m',   # 0 - sem cores
'\033[0;30;41m',  # 1 - vermelho
'\033[0;30;42m',  # 2 - verde
'\033[0;30;43m',  # 3 - amerelo
'\033[0;30;44m',  # 4 - azul
'\033[0;30;45m',  # 5 - rosa
'\033[7;30m',     # 6 - preto
     )
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input(f'Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)

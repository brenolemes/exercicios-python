def leiaDinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print(f'\033[0;31mERRO: \"{n}\" é um valor numérico inválido.\033[m')
        else:
            ok = True
            return float(n)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

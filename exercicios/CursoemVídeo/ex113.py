'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
possibilidade da digitação de um número de tipo inválido. Aproveite e crie também
uma função leiaFloat() com a mesma funcionalidade.
'''


def leiaInt(msg):
    ok = False
    valor = 0
    while not ok:
        try:
            n = int(input(msg))
            valor = int(n)
            ok = True
        except (ValueError, TypeError):   # o que eu não puder alterar nos erros
            print(f'\033[0;31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mO usuário preferiu não informar os dados!\033[m')
            continue
        else:
            return valor


def leiaFloat(msg):
    ok = False
    valor = 0
    while not ok:
        n = str(input(msg)).strip().replace(',', '.')   # o que eu puder alterar nos erros
        try:
            valor = float(n)
            ok = True
        except ValueError:  # o que eu não puder alterar nos erros
            print(f'\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mO usuário preferiu não informar os dados!\033[m')
            break
        else:
            return valor


# Programa principal
i = leiaInt('Digite um inteiro: ')
print(f'Você digitou o inteiro {i}')
f = leiaFloat('Digite um real: ')
print(f'Você digitou o real {f}')

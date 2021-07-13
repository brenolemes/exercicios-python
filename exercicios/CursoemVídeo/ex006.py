# Crie um algorítmo que leia um número e mostre o seu dobro, seu triplo e sua raíz quadrada
# pow(n, (1/2) == outra forma de calcular potência

n1 = int(input('Dígite um valor: '))
print('O dobro de {} é {}; \no triplo de {} é {}; \nE a raíz quadrada de {} é {:.2f}'.format(n1, (n1 * 2), n1, (n1 * 3), n1, (n1 ** (1/2))))


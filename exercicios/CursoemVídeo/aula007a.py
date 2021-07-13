# OPERADORES ARITMÉTICOS
# {:.2f} == Duas casas após a virgula
# end=' ' == Para não quebrar a linha
# \n == Para quebrar a linha

n1 = int(input('Dígite um valor: '))
n2 = int(input('Dìgite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma entre {} e {} é {},'.format(n1, n2, s), end=' ')
print('a multiplicação é {}, a divisão é {:.2f}, a divisão inteira é {} e a exponênciação é {}'.format(m, d, di, e))

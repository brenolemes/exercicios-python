# Desenvolva um progra que leia o comprimeto de três retas e diga ao usuário se elas podem ou não formar um triângulo

print('-==-' * 20)
print('ANALISANDO SE TRÊS SEGMENTOS FORMAM UM TRIÂNGULO')
print('-==-' * 20)
r1 = float(input('Qual é o primeiro segmento: '))
r2 = float(input('Qual é o segundo segmento: '))
r3 = float(input('Qual é o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!!')
else:
    print('Os segmentos acima NÃO podem formar um Triângulo!!')


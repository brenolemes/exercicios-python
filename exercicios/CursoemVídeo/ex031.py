'''desenvolva um programa que paergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas '''

distancia = float(input('Qual distâcia percorrida? '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print(f'O valor da viagem será de R${valor}')

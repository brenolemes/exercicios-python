# Escreva um programa que pergute a quantidade de km percorridos por um carro aluagdo e a quantidade...
# ...de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por km# rodado

km = float(input('Quantos km foram percorridos com o carro alugado? '))
d = int(input('Por quantos dias ele foi alugado? '))
valorPorKm = km * 0.15
valorPorDia = d * 60
valorTotal = valorPorKm + valorPorDia
print('O valor por dia é de R${:.2f} por km é de R${:.2f} e o total fica R${:.2f}'.format(valorPorDia, valorPorKm, valorTotal))

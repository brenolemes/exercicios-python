# Crie um prgrama que leia quanto reias uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

real = float(input('Quanto em reais você tem na carteira? R$'))
dolar = real / 5.61
euro = real / 6.68
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))

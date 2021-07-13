### Crie um programa que leia sua altura e largura em metros, calcu-le sua area e a quantide de tinta necessária para pintá-la, sabendo que uma litro de tinta, pinta uma area de 2m²

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede '))
area = altura * largura
print('Sua parede tem a dimensão de {}x{} e sua area é de {:.2f}m²'.format(altura, largura, area))
print('Será necessário {:.2f} lintros de tinta para pintar essa parede'.format(area / 2))

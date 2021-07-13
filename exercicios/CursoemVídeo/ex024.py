# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'Santo'

#cidade = str(input('Dígite em qual cidade vc mora: ')).strip()
#dividido = cidade.split()
#print('Santo' in dividido[0])

cidade = str(input('Dígite em qual cidade vc mora: ')).strip()
print(cidade[:5].lower() == 'santo')

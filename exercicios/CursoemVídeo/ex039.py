''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- se é a hora de se alistar
- Se já passou do tempo do alistamento
- Seu programa também deve mostrar o tempo que falta ou que passou do prazo '''
from datetime import date
from time import sleep

print('\033[1;33m--==--\033[m' * 20)
print('\033[1;34mANALISANDO ALISTAMENTO MILITAR\033[m')
print('\033[1;33m--==--\033[m' * 20)

nascimento = int(input('Qual ano vc nasceu? '))
sexo = str(input('''Qual é o seu sexo? 
[1] para MASCULINO:
[2] para FEMENINO: 
'''))

ano = date.today().year
idade = ano - nascimento

print(f'Você tem {idade} anos !!')

if idade < 18:
    faltam = 18 - idade
    print('\033[1;33mANALISANDO...\033[m')
    sleep(2)
    print(f'''Você vai se alistar daqui {faltam} anos!!')
    em {ano + faltam}''')
elif idade == 18:
    print('\033[1;33mANALISANDO...\033[m')
    sleep(2)
    print('Você está na idade para se alistar!!')
else:
    passou = idade - 18
    print('\033[1;33mANALISANDO...\033[m')
    sleep(2)
    print(f'Já passou {passou} anos que vc podia se alistar!!')



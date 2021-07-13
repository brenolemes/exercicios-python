# Condições

# Estrutura composta de condição
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 +n2) / 2
print(f'Sua média foi {m}')

if m >= 7:
    print('Parabens!!!')
else:
    print('Você reprovou!!')

# Estrutura simples de condição

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 +n2) / 2
print(f'Sua média foi {m}')
print('Parabens!!' if m >= 7 else 'Você reprovou!!')

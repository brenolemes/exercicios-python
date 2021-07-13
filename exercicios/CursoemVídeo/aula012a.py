# Condições aninhadas


nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Breno':
    print(f'Que nome bonito você tem !!')
elif nome == 'Maria' or nome == 'João' or nome == 'Pedro' or nome == 'Paulo':
    print(f'que nome popular você tem !!')
else:
    print(f'Seu nome é bem normal !!')
print(f'Tenha um bom dia, {nome} !!')

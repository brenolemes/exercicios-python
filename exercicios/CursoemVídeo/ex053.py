'''Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconciderando os espaços. Exemplos:
- Apos a sopa
- a sacada da casa
- A torre da derrota
- O lobo ama o bolo
- Anotaram a data da maratona'''

frase = str(input('Digite uma frase qualquer: ')).strip().upper()

palavra = frase.split()
junto = ''.join(palavra) # Eu splitei as palavras primeiro, pra depois junta-las
inverso= ''

# inverso = junto[::-1] # Da pra fazer desse forma também

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)

if inverso == junto:
    print('Esta frase é um palíndromo')
else:
    print('Esta frase não é um palíndromo')

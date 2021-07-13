# Crie um programa que leia qualquer frase e mostre:
# Quatos 'a' tem na frase
# Em qual indice aparece o primeiro 'a'
# Em qual indice aparece o segundo 'a'

frase = str(input('Dígite uma frase: ')).strip()
print(f"""A letra "a" aparece {frase.upper().count('A')} vezes""")
print(f"A primeira letra 'a' aparece na posição {frase.upper().find('A') + 1}")
print(f"A ultima letra 'a' aparece na posição {frase.upper().rfind('A') + 1}")

# Crie umprograma que leia um nome completo de uma pessoa e diga se ela tem 'Silva' no nome
nome = str(input('Dígite seu nome completo: ')).strip()
print(f"Seu nome tem Silva? {'SILVA' in nome.upper()}")


